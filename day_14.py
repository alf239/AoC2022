#!/usr/bin/env python3

import aoc

task = aoc.get_input(14)
example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def parse_dot(dot):
    start = dot.split(",")
    [x, y] = [int(n) for n in start]
    return x, y


def parse_map(inp):
    m = {}
    for line in inp.splitlines():
        dots = line.split(" -> ")
        dot = dots[0]
        x, y = parse_dot(dot)
        m[(x, y)] = "#"
        for dot in dots[1:]:
            xt, yt = parse_dot(dot)
            dx = sign(xt - x)
            dy = sign(yt - y)
            while x != xt or y != yt:
                x += dx
                y += dy
                m[(x, y)] = "#"
    return m


def fall(x, y, m):
    if (x, y + 1) not in m:
        return True, x, y + 1
    if (x - 1, y + 1) not in m:
        return True, x - 1, y + 1
    if (x + 1, y + 1) not in m:
        return True, x + 1, y + 1
    return False, x, y


def part1(inp):
    m = parse_map(inp)

    void = max(y for _, y in m) + 1

    while True:
        x, y = 500, 0
        while y < void:
            fell, nx, ny = fall(x, y, m)
            if not fell:
                m[(x, y)] = "o"
                break
            x = nx
            y = ny
        else:
            break

    return len(list(c for c in m if m[c] == 'o'))


def part2(inp):
    m = parse_map(inp)

    floor = max(y for _, y in m) + 2

    while (500, 0) not in m:
        x, y = 500, 0
        while True:
            if y + 1 == floor:
                m[(x, y)] = "o"
                break
            fell, nx, ny = fall(x, y, m)
            if not fell:
                m[(x, y)] = "o"
                break
            x = nx
            y = ny

    return len(list(c for c in m if m[c] == 'o'))


assert part1(example) == 24
print("Part 1:", part1(task))

assert part2(example) == 93
print("Part 2:", part2(task))
