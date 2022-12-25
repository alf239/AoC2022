#!/usr/bin/env python3

import aoc

task = aoc.get_input(8)
example = """30373
25512
65332
33549
35390"""


def parse(ss):
    return [[int(c) for c in s] for s in ss.splitlines()]


def height(m, x, y):
    if x < 0:
        return -1
    if y < 0:
        return -1
    if y >= len(m[0]):
        return -1
    if x >= len(m):
        return -1
    return m[x][y]


def can_see(m, x, y, dx, dy):
    me = height(m, x, y)
    for i in range(1, len(m) + 1):
        h = height(m, x + i * dx, y + i * dy)
        if h == -1:
            return True
        if h >= me:
            return False
    else:
        raise Exception("Fallen off the cliff!")


def visible(m, x, y):
    return (
        can_see(m, x, y, -1, 0) or
        can_see(m, x, y, 1, 0) or
        can_see(m, x, y, 0, -1) or
        can_see(m, x, y, 0, 1)
    )


def score(m, x, y, dx, dy):
    me = height(m, x, y)
    t = 0
    for i in range(1, len(m) + 1):
        h = height(m, x + i * dx, y + i * dy)
        if h == -1:
            return t
        t = t + 1
        if h >= me:
            return t


def scenic_score(m, x, y):
    up = score(m, x, y, -1, 0)
    dn = score(m, x, y, 1, 0)
    lt = score(m, x, y, 0, -1)
    rt = score(m, x, y, 0, 1)
    return up * dn * lt * rt


def part1_(m):
    W = len(m[0])
    H = len(m)
    visibility = [[1 if visible(m, x, y) else 0 for y in range(W)] for x in range(H)]
    return sum(sum(ln) for ln in visibility)


def part1(s):
    m = parse(s)
    return part1_(m)


def part2(s):
    m = parse(s)
    return max(max(scenic_score(m, x, y) for x in range(len(m))) for y in range(len(m[0])))


m = parse(example)
assert visible(m, 1, 1)
assert visible(m, 1, 2)
assert not visible(m, 1, 3)
assert visible(m, 2, 1)
assert visible(m, 2, 3)
assert not visible(m, 2, 2)
p1 = part1(example)
assert p1 == 21
print("Part 1:", part1(task))

assert part2(example) == 8
print("Part 2:", part2(task))
