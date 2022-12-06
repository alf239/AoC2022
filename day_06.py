import aoc

task = aoc.get_input(6)
example = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""


def all_diff(s):
    return len(set(s)) == len(s)


def part1(s):
    for i in range(len(s) - 4):
        if all_diff(s[i:i+4]):
            return i + 4
    return -1


def part2(s):
    for i in range(len(s) - 14):
        if all_diff(s[i:i+14]):
            return i + 14
    return -1


assert part1(example) == 10
print("Part 1:", part1(task))

assert part2(example) == 29
print("Part 2:", part2(task))
