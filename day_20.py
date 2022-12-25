#!/usr/bin/env python3

import aoc

task = aoc.get_input(20)
example = """1
2
-3
3
-2
0
4"""


def doubly_linked_list(n):
    return [(i + 1) % n for i in range(n)], [(i - 1) % n for i in range(n)]


def move(entry, next, prev, lookup):
    a = prev[entry]
    b = next[entry]
    next[a] = b
    prev[b] = a

    steps = lookup[entry] % (len(next) - 1)
    for i in range(steps):
        a = next[a]

    b = next[a]
    next[a] = entry
    next[entry] = b
    prev[b] = entry
    prev[entry] = a


def read_result(nrs, next):
    n = len(nrs)  # == len(next)
    curr = nrs.index(0)
    for i in range(1000 % n):
        curr = next[curr]
    x1 = nrs[curr]
    for i in range(1000 % n):
        curr = next[curr]
    x2 = nrs[curr]
    for i in range(1000 % n):
        curr = next[curr]
    x3 = nrs[curr]
    return x1 + x2 + x3


def part1(inp):
    nrs = [int(s) for s in inp.splitlines()]
    n = len(nrs)

    next, prev = doubly_linked_list(n)
    for entry in range(n):
        move(entry, next, prev, nrs)

    return read_result(nrs, next)


def part2(inp):
    nrs = [int(s) * 811589153 for s in inp.splitlines()]
    n = len(nrs)

    next, prev = doubly_linked_list(n)
    for i in range(10):
        for entry in range(n):
            move(entry, next, prev, nrs)

    return read_result(nrs, next)


assert part1(example) == 3
print("Part 1:", part1(task))

assert part2(example) == 1623178306
print("Part 2:", part2(task))
