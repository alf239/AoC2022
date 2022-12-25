#!/usr/bin/env python3

import aoc

task = aoc.get_input(23)
example = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""

DIRS = [
    ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
    ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
    ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
    ((1, 0), [(1, -1), (1, 0), (1, 1)]),
]


def bounding_rectangle(m):
    mnx = None
    mxx = None
    mny = None
    mxy = None
    for x, y in m:
        if mnx is None or mnx > x:
            mnx = x
        if mxx is None or mxx < x:
            mxx = x
        if mny is None or mny > y:
            mny = y
        if mxy is None or mxy < y:
            mxy = y
    return mnx, mny, mxx, mxy


def part1(inp, n, trace=False):
    m, x_size, y_size = parse(inp)

    if trace:
        print("== Initial State ==")
        print_map(m, x_size, y_size)
        print()

    for i in range(n):
        m, _ = movement(m, i)
        if trace:
            print(f"== End of Round {i + 1} ==")
            print_map(m, x_size, y_size)
            print()

    mnx, mny, mxx, mxy = bounding_rectangle(m)
    return (mxy - mny + 1) * (mxx - mnx + 1) - len(m)


def parse(inp):
    m = set()
    y = 0
    lines = inp.splitlines()
    x_size = -1
    y_size = len(lines)
    for s in lines:
        x_size = max(len(s), x_size)
        for x in range(x_size):
            if s[x] == '#':
                m.add((x, y))
        y += 1
    return m, x_size, y_size


def movement(m, i):
    moved = False
    proposals = {}
    for x, y in m:
        if all(dx == 0 and dy == 0 or (x + dx, y + dy) not in m for dx in range(-1, 2) for dy in range(-1, 2)):
            proposals[(x, y)] = [(x, y)]
            continue

        for j in range(4):
            move, checks = DIRS[(i + j) % 4]
            if not any((x + dx, y + dy) in m
                       for dx, dy in checks):
                proposal = (x + move[0], y + move[1])
                offered = proposals.setdefault(proposal, [])
                offered.append((x, y))
                break
        else:
            proposals[(x, y)] = [(x, y)]
    m1 = set()
    for goal, candidates in proposals.items():
        if len(candidates) > 1:
            for elf in candidates:
                m1.add(elf)
        else:
            if candidates[0] != goal:
                moved = True
            m1.add(goal)
    assert len(m1) == len(m)
    return m1, moved


def print_map(m1, x_size, y_size):
    for y in range(y_size):
        for x in range(x_size):
            if (x, y) in m1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part2(inp):
    m, x_size, y_size = parse(inp)

    i = 0
    while True:
        m, moved = movement(m, i)
        i += 1
        if not moved:
            return i


def test_moves():
    m, x_size, y_size = parse(""".....
..##.
..#..
.....
..##.
.....""")
    m1, x_size1, y_size1 = parse("""..##.
.....
..#..
...#.
..#..
.....""")
    assert movement(m, 0)[0] == m1
    m2, x_size2, y_size2 = parse(""".....
..##.
.#...
....#
.....
..#..""")
    assert movement(m1, 1)[0] == m2
    m3, x_size3, y_size3 = parse("""..#..
....#
#....
....#
.....
..#..""")
    assert movement(m2, 2)[0] == m3


test_moves()

assert part1(example, 10) == 110
print("Part 1:", part1(task, 10))

assert part2(example) == 20
print("Part 2:", part2(task))
