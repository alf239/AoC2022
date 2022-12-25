#!/usr/bin/env python3

import aoc
import hashlib

task = aoc.get_input(17).strip()
W = 7
shapes = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
example = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


def parse_part(ss):
    part = []
    y = 0
    lines = ss.splitlines()
    h = len(lines)
    for s in lines:
        x = 0
        for c in s:
            if c == "#":
                part.append((x, h - y - 1))
            x += 1
        y += 1
    part.reverse()
    return part


def parse_parts(ss):
    for p in ss.split("\n\n"):
        yield parse_part(p)


def model_stack(inp, n, parts, repetition):
    seen = {}
    new = True
    xp = -1
    yp = -1
    p = 0
    part = []
    t = 0
    stack = set()
    h = 0
    fallen = 0
    while fallen < n:
        if new:
            xp = 2
            yp = h + 3
            part = parts[p]
            p = (p + 1) % len(parts)
            new = False

        c = inp[t % len(inp)]
        t += 1

        if c == '>':
            for x, y in part:
                if xp + x + 1 >= W:
                    break
                if (xp + x + 1, yp + y) in stack:
                    break
            else:
                xp += 1
        elif c == '<':
            for x, y in part:
                if xp + x - 1 < 0:
                    break
                if (xp + x - 1, yp + y) in stack:
                    break
            else:
                xp -= 1
        else:
            raise Exception(f"Unknown command {c} at t = {t}")

        for x, y in part:
            if yp + y - 1 < 0:
                break
            if (xp + x, yp + y - 1) in stack:
                break
        else:
            yp -= 1
            continue

        for x, y in part:
            stack.add((xp + x, yp + y))
            if yp + y + 1 > h:
                h = yp + y + 1

        fallen += 1
        window = 200
        if h > window and repetition:
            c = p
            for dy in range(window):
                for x in range(W):
                    c = c * 2 + (1 if (x, h - dy) in stack else 0)
            if c in seen:
                nn, hh = seen[c]
                print(f"Found repetition at {fallen}, match {fallen - nn}, part {p}, h = {hh}, dh = {h - hh}")
                return fallen, fallen - nn, h, h - hh
            seen[c] = (fallen, h)
        if fallen % 100000 == 0:
            print(f"{fallen} figures fallen, seen {len(seen)} configurations")
        new = True
    return h, stack


def part1(inp, n):
    parts = [p for p in parse_parts(shapes)]
    h, stack = model_stack(inp, n, parts, False)
    return h


def part2(inp, n):
    parts = [p for p in parse_parts(shapes)]
    fallen, dn, h, dh = model_stack(inp, n, parts, True)
    to_model = n - fallen
    simplen = to_model % dn + fallen
    h1, _ = model_stack(inp, simplen, parts, False)
    result = h1 + to_model // dn * dh
    return result


assert part1(example, 2022) == 3068
assert part1(task, 2022) == 3100
print("Part 1:", part1(task, 2022))

assert part2(example, 1000000000000) == 1514285714288
print("Part 2:", part2(task, 1000000000000))
