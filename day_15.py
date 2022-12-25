#!/usr/bin/env python3

import aoc

task = aoc.get_input(15)
example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def parse_nr(s):
    return int(s.split("=")[1].split(",")[0].split(":")[0])


def parse(inp):
    data = []
    for s in inp.splitlines():
        [_, _, sx, sy, _, _, _, _, bx, by] = s.split(" ")
        data.append(((parse_nr(sx), parse_nr(sy)), (parse_nr(bx), (parse_nr(by)))))
    return data


def part1(inp, y):
    data = parse(inp)
    beacons = set()
    safe = set()
    for (sx, sy), (bx, by) in data:
        if by == y:
            beacons.add(bx)
        d = abs(bx - sx) + abs(by - sy)
        dy = abs(sy - y)
        rng = d - dy
        if rng < 0:
            continue
        for x in range(sx - rng, sx + rng + 1):
            safe.add(x)
    return len(safe) - len(beacons)


def part2(inp, n):
    data = parse(inp)
    ss = [(sx, sy, abs(bx - sx) + abs(by - sy)) for (sx, sy), (bx, by) in data]
    y = 0
    while y <= n:
        x = 0
        while x <= n:
            for sx, sy, d in ss:
                distance = abs(x - sx) + abs(y - sy)
                if distance <= d:
                    x += d - distance
                    break
            else:
                return x * 4000000 + y
            x += 1
        # if y % 100000 == 0:
        #     print(y)
        y += 1

    raise Exception("Oh I cannot find anything!")


assert part1(example, 10) == 26
print("Part 1:", part1(task, 2000000))

assert part2(example, 20) == 56000011
print("Part 2:", part2(task, 4000000))
