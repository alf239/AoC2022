#!/usr/bin/env python3

from collections import deque

import aoc

task = aoc.get_input(24)
example = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


def neighbours(x, y):
    return [(x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def safe(m, h, w, horz, vert, t, x, y):
    if 0 > x or x >= w + 2 or 0 > y or y >= h + 2 or m[y][x] == '#':
        return False
    if x in vert:
        for yb, dy in vert[x]:
            if (yb + t * dy - 1) % h + 1 == y:
                return False
    if y in horz:
        for xb, dx in horz[y]:
            if (xb + t * dx - 1) % w + 1 == x:
                return False
    return True


def time(inp, t0, fwd):
    m = inp.splitlines()
    horz = {}
    vert = {}
    y = 0
    for s in m:
        x = 0
        for c in s:
            if c == '<':
                horz.setdefault(y, []).append((x, -1))
            elif c == '>':
                horz.setdefault(y, []).append((x, 1))
            if c == '^':
                vert.setdefault(x, []).append((y, -1))
            elif c == 'v':
                vert.setdefault(x, []).append((y, 1))
            x += 1
        y += 1
    height = len(m)
    h = height - 2
    width = len(m[0])
    w = width - 2

    seen = set()
    work = deque()
    if fwd:
        y_goal = height - 1
        work.append((t0, 1, 0))
    else:
        y_goal = 0
        work.append((t0, width - 2, height - 1))
    while work:
        t, x, y = work.popleft()
        if (t, x, y) in seen:
            continue
        seen.add((t, x, y))
        if y == y_goal:
            return t
        for x1, y1 in neighbours(x, y):
            if safe(m, h, w, horz, vert, t + 1, x1, y1):
                work.append((t + 1, x1, y1))
    raise Exception('Out of work, but no cigar!')


def part1(inp):
    return time(inp, 0, fwd=True)


def part2(inp):
    t1 = time(inp, 0, fwd=True)
    t2 = time(inp, t1, fwd=False)
    return time(inp, t2, fwd=True)


assert part1(example) == 18
print("Part 1:", part1(task))

assert part2(example) == 54
print("Part 2:", part2(task))
