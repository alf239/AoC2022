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


def part1(inp):
    cubes1 = [[int(x) for x in s.split(",")] for s in inp.splitlines()]
    cubes = set((x[0], x[1], x[2]) for x in cubes1)
    i = 0
    for x, y, z in cubes:
        if (x + 1, y, z) not in cubes: i += 1
        if (x - 1, y, z) not in cubes: i += 1
        if (x, y + 1, z) not in cubes: i += 1
        if (x, y - 1, z) not in cubes: i += 1
        if (x, y, z + 1) not in cubes: i += 1
        if (x, y, z - 1) not in cubes: i += 1
    return i


def is_free(x, y, z, cubes, cavity):
    seen = set()
    work = deque()
    x0, y0, z0 = x, y, z
    work.append((0, x, y, z))
    maxi = 0
    while work:
        i, x, y, z = work.pop()
        if i > maxi: maxi = i
        if (x, y, z) in cubes: continue
        if (x, y, z) in cavity: return False
        if (x, y, z) in seen: continue
        seen.add((x, y, z))
        if (x + 1, y, z) not in cubes: work.append((i + 1, x + 1, y, z))
        if (x - 1, y, z) not in cubes: work.append((i + 1, x - 1, y, z))
        if (x, y + 1, z) not in cubes: work.append((i + 1, x, y + 1, z))
        if (x, y - 1, z) not in cubes: work.append((i + 1, x, y - 1, z))
        if (x, y, z + 1) not in cubes: work.append((i + 1, x, y, z + 1))
        if (x, y, z - 1) not in cubes: work.append((i + 1, x, y, z - 1))
        if abs(x - x0) + abs(y - y0) + abs(z - z0) > 50:
            return True

    cavity.update(seen)
    return False


def part2(inp):
    cubes1 = [[int(x) for x in s.split(",")] for s in inp.splitlines()]
    cavity = set()
    cubes = set((x[0], x[1], x[2]) for x in cubes1)
    i = 0
    for x, y, z in cubes:
        if is_free(x + 1, y, z, cubes, cavity): i += 1
        if is_free(x - 1, y, z, cubes, cavity): i += 1
        if is_free(x, y + 1, z, cubes, cavity): i += 1
        if is_free(x, y - 1, z, cubes, cavity): i += 1
        if is_free(x, y, z + 1, cubes, cavity): i += 1
        if is_free(x, y, z - 1, cubes, cavity): i += 1
    return i


assert part1(example) == 64
print("Part 1:", part1(task))

assert part2(example) == 58
print("Part 2:", part2(task))
