import aoc
from collections import deque
from heapq import heappush, heappop

infinity = 10000000000

task = aoc.get_input(16)
example = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def parse_nr(s):
    return int(s.split("=")[1].split(",")[0].split(":")[0])


def parse(inp):
    data = {}
    for s in inp.splitlines():
        [_, name, _, _, rate, _, _, _, _, *tunnels] = s.split(" ")
        data[name] = (
            int(rate.split("=")[1].split(";")[0]),
            [t.split(",")[0] for t in tunnels])
    idx = {}
    i = 0
    for n, _ in data.items():
        idx[n] = i
        i += 1
    optimised = []
    for n, (rate, tunnels) in data.items():
        assert idx[n] == len(optimised)
        mask = 1 << idx[n]
        optimised.append((mask, rate, [idx[t] for t in tunnels]))
        i += 1
    return idx, optimised


def part1(inp):
    n = 30
    names, data = parse(inp)
    work = deque()
    work.append((1, names["AA"], 0, 0))
    best = {}
    while work:
        t, curr, opened, released = work.pop()
        if t > n:
            continue
        bestsofar = best.setdefault((t, curr, opened), -1)
        if bestsofar >= released:
            continue
        best[(t, curr, opened)] = released
        mask, rate, tunnels = data[curr]
        if rate > 0 and (opened & mask) == 0:
            newopen = opened | mask
            work.appendleft((t + 1, curr, newopen, released + rate * (n - t)))
        for tunnel in tunnels:
            work.appendleft((t + 1, tunnel, opened, released))
    return max(r for n, r in best.items())


def fw(data):
    dist = [[infinity for _ in range(len(data))] for _ in range(len(data))]
    for i in range(len(data)):
        mask, _, tunnels = data[i]
        for t in tunnels:
            dist[i][t] = 1
        dist[i][i] = 0
    for k in range(len(data)):
        for i in range(len(data)):
            for j in range(len(data)):
                chance = dist[i][k] + dist[k][j]
                if dist[i][j] > chance:
                    dist[i][j] = chance
    return dist


def offer(a1, a2, opened, released, t, work, best, n):
    best_so_far = best.setdefault((a1, a2, opened, t), -1)
    if released <= best_so_far:
        return
    for tt in range(t, n + 1):
        best[(a1, a2, opened, tt)] = max(released, best.setdefault((a1, a2, opened, tt), -1))
    work.append((infinity - released, t, a1, a2, opened))


def part2(inp):
    step = 0
    n = 26
    names, data = parse(inp)
    all_open = 0
    for mask, r, _ in data:
        if r > 0:
            all_open |= mask

    dist = fw(data)
    routes = [[(j, dist[i][j] + 1)
               for j in range(len(data))
               if dist[i][j] < infinity  # reachable
               and data[j][1] > 0  # is worth reaching
               and i != j
               ] for i in range(len(data))]

    work = []
    start = (names["AA"], 0)
    best = {}
    offer(start, start, 0, 0, 0, work, best, n)
    while work:
        pressure, t, a1, a2, opened = heappop(work)
        released = infinity - pressure

        if opened == all_open:
            continue

        step += 1
        if step % 1000000 == 0:
            print(f"step {step}; t = {t}, work left: {len(work)}")

        v1, t1 = a1
        v2, t2 = a2

        if t1 > t2:
            v1, v2 = v2, v1
            t1, t2 = t2, t1

        time_left = n - t
        if t1 == 0 and t2 == 0:
            for next_v1, next_dist1 in routes[v1]:
                if is_open(data, opened, next_v1) and time_left >= next_dist1:
                    mask1, r1, _ = data[next_v1]
                    pv_me = r1 * (time_left - next_dist1)
                    for next_v2, next_dist2 in routes[v2]:
                        if is_open(data, opened, next_v2) and time_left >= next_dist2:
                            if next_v1 != next_v2 and (v1 != v2 or next_v1 < next_v2):
                                mask2, r2, _ = data[next_v2]
                                ff = min(next_dist1, next_dist2)
                                pv_el = r2 * (time_left - next_dist2)
                                offer((next_v1, next_dist1 - ff), (next_v2, next_dist2 - ff), opened | mask1 | mask2,
                                      released + pv_me + pv_el, t + ff, work, best, n)
                    offer((next_v1, 0), (v2, 0), opened | mask1, released + pv_me, t + next_dist1, work, best, n)
            for next_v2, next_dist2 in routes[v2]:
                if is_open(data, opened, next_v2) and time_left >= next_dist2:
                    mask2, r2, _ = data[next_v2]
                    ff = next_dist2
                    pv_el = r2 * (time_left - next_dist2)
                    offer((v1, 0), (next_v2, next_dist2 - ff), opened | mask2, released + pv_el, t + ff, work, best,
                          n)

        elif t1 == 0:
            for next_v, next_dist in routes[v1]:
                if is_open(data, opened, next_v) and time_left >= next_dist:
                    mask1, r1, _ = data[next_v]
                    ff = min(t2, next_dist)
                    pv_me = r1 * (time_left - next_dist)
                    offer((v2, t2 - ff), (next_v, next_dist - ff), opened | mask1, released + pv_me, t + ff, work, best,
                          n)

        else:
            raise Exception("Both en route, should be optimized away")

    result = max(r for _, r in best.items())
    return result


def is_open(data, opened, valve):
    return (opened & data[valve][0]) == 0


assert part1(example) == 1651
print("Part 1:", part1(task))

assert part2(example) == 1707
print("Example passed for part 2")
print("Part 2:", part2(task))
