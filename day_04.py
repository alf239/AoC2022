import aoc

task = aoc.get_input(4)
example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def interesting(s):
    [a,  b] = s.split(',')
    aa = [int(x) for x in a.split('-')]
    bb = [int(x) for x in b.split('-')]
    bina = aa[0] <= bb[0] and aa[1] >= bb[1]
    ainb = aa[0] >= bb[0] and aa[1] <= bb[1]
    result = bina or ainb
    return result


def sizeit(s):
    [a,  b] = s.split(',')
    aa = [int(x) for x in a.split('-')]
    bb = [int(x) for x in b.split('-')]
    overlap = [x for x in set.intersection(set(range(aa[0], aa[1] + 1)), set(range(bb[0], bb[1] + 1)))]
    return len(overlap)


def part1(inp):
    return sum([1 if interesting(ln) else 0 for ln in inp.splitlines()])


def part2(inp):
    return sum([1 if sizeit(ln) else 0 for ln in inp.splitlines()])


def sanity1():
    assert part1(example) == 2


def sanity2():
    assert part2(example) == 4


sanity1()
print("Part 1:", part1(task))

sanity2()
print("Part 2:", part2(task))



