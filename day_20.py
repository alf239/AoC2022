import aoc

task = aoc.get_input(20)
example = """1
2
-3
3
-2
0
4"""


def move(entry, next, prev):
    a = prev[entry]
    b = next[entry]
    next[a] = b
    prev[b] = a

    for i in range(abs(entry[1]) % (len(next) - 1)):
        if entry[1] > 0:
            a = next[a]
            b = next[b]
        else:
            a = prev[a]
            b = prev[b]

    next[a] = entry
    next[entry] = b
    prev[b] = entry
    prev[entry] = a


def read_result(entries, n, next):
    for entry in entries:
        if entry[1] == 0:
            point = entry
            break
    else:
        raise Exception("Cannot find the zero!")
    for i in range(1000 % n):
        point = next[point]
    x1 = point[1]
    for i in range(1000 % n):
        point = next[point]
    x2 = point[1]
    for i in range(1000 % n):
        point = next[point]
    x3 = point[1]
    result = x1 + x2 + x3
    return result


def part1(inp):
    nrs = [int(s) for s in inp.splitlines()]
    n = len(nrs)
    entries = [(i, nrs[i]) for i in range(n)]

    next = {}
    prev = {}
    for i in range(len(nrs)):
        next[entries[i]] = entries[(i + 1) % n]
        prev[entries[i]] = entries[(i + n - 1) % n]

    for entry in entries:
        move(entry, next, prev)

    result = read_result(entries, n, next)
    return result


def part2(inp):
    nrs = [int(s) for s in inp.splitlines()]
    n = len(nrs)
    entries = [(i, nrs[i] * 811589153) for i in range(n)]

    next = {}
    prev = {}
    for i in range(len(nrs)):
        next[entries[i]] = entries[(i + 1) % n]
        prev[entries[i]] = entries[(i + n - 1) % n]

    for i in range(10):
        for entry in entries:
            move(entry, next, prev)

    result = read_result(entries, n, next)
    return result


assert part1(example) == 3
print("Part 1:", part1(task))

assert part2(example) == 1623178306
print("Part 2:", part2(task))
