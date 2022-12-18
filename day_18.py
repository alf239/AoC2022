from collections import deque

import aoc

task = aoc.get_input(18)
example = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def parse_input(inp):
    cubes1 = [[int(x) for x in s.split(",")] for s in inp.splitlines()]
    cubes = set((x[0], x[1], x[2]) for x in cubes1)
    return cubes


def neighbours(x, y, z):
    return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]


def part1(inp):
    cubes = parse_input(inp)
    i = 0
    for x, y, z in cubes:
        for x1, y1, z1 in neighbours(x, y, z):
            if (x1, y1, z1) not in cubes:
                i += 1
    return i


def is_free(x, y, z, cubes, cavity):
    seen = set()
    work = deque()
    x0, y0, z0 = x, y, z
    work.append((x, y, z))
    while work:
        x, y, z = work.pop()
        if (x, y, z) in cubes: continue
        if (x, y, z) in cavity: return False
        if (x, y, z) in seen: continue
        seen.add((x, y, z))
        if abs(x - x0) + abs(y - y0) + abs(z - z0) > 60:
            return True
        work.extend(neighbours(x, y, z))

    cavity.update(seen)
    return False


def part2(inp):
    cubes = parse_input(inp)
    cavity = set()
    i = 0
    for x, y, z in cubes:
        for x1, y1, z1 in neighbours(x, y, z):
            if is_free(x1, y1, z1, cubes, cavity):
                i += 1
    return i


assert part1(example) == 64
print("Part 1:", part1(task))

assert part2(example) == 58
print("Part 2:", part2(task))
