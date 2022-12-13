import functools

import aoc
import itertools

task = aoc.get_input(13)
example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def compare(a, b):
    # print(f"right_order({a}, {b})")
    if type(a) is list and type(b) is list:
        for aa, bb in itertools.zip_longest(a, b, fillvalue=-1):
            c = compare(aa, bb)
            if c < 0:
                return -1
            if c > 0:
                return 1
        else:
            return 0
    if type(a) is list:
        return compare(a, [b])
    if type(b) is list:
        return compare([a], b)
    return -1 if a < b else 1 if a > b else 0


def part1(inp):
    pairs = [(eval(p.splitlines()[0]), eval(p.splitlines()[1])) for p in inp.split("\n\n")]
    proper = []
    i = 1
    for a, b in pairs:
        # print()
        if compare(a, b) == -1:
            proper.append(i)
        i += 1
    return sum(proper)


def part2(inp):
    pairs = [eval(p) for p in inp.splitlines() if p != ""]
    pairs.append([[2]])
    pairs.append([[6]])
    pairs.sort(key=functools.cmp_to_key(compare))
    return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)


assert part1(example) == 13
print("Part 1:", part1(task))

assert part2(example) == 140
print("Part 2:", part2(task))
