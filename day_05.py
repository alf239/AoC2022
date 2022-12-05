import aoc

task = aoc.get_input(5)
example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_command(s):
    [_, nr, _, fr, _, to] = s.split(" ")
    f = int(fr) - 1
    t = int(to) - 1
    n = int(nr)
    return n, f, t


def parse(inp):
    [a, b] = inp.split("\n\n")
    at = list(reversed(a.splitlines()))
    size = (len(at[0]) + 2) // 4
    stacks = [[] for _ in range(size)]
    for s in at[1:]:
        for i in range(size):
            idx = i * 4 + 1
            if idx < len(s) and s[idx] != " ":
                stacks[i].append(s[idx])
    return stacks, [parse_command(s) for s in b.splitlines()]


def read_output(stacks):
    return "".join(s[-1] for s in stacks)


def part1(inp):
    stacks, commands = parse(inp)
    for n, f, t in commands:
        for i in range(int(n)):
            crate = stacks[f].pop()
            stacks[t].append(crate)
    return read_output(stacks)


def part2(inp):
    stacks, commands = parse(inp)
    for n, f, t in commands:
        crates = stacks[f][-n:]
        stacks[f] = stacks[f][:-n]
        stacks[t].extend(crates)
    return read_output(stacks)


assert part1(example) == "CMZ"
print("Part 1:", part1(task))

assert part2(example) == "MCD"
print("Part 2:", part2(task))
