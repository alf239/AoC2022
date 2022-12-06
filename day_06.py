import aoc

task = aoc.get_input(6)
example = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""


def all_diff(s):
    return len(set(s)) == len(s)


def part(s, n):
    for i in range(len(s) - n):
        if all_diff(s[i:i+n]):
            return i + n
    return -1


def part1(s):
    return part(s, 4)


def part2(s):
    return part(s, 14)


assert part1(example) == 10
print("Part 1:", part1(task))

assert part2(example) == 29
print("Part 2:", part2(task))
