import aoc

task = aoc.get_input(10)
small = """noop
addx 3
addx -5"""
example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def parse(ss):
    return [s.split(" ") for s in ss.splitlines()]


def check_signal(x, pc):
    if (pc - 20) % 40 == 0:
        # print(pc, x, pc * x)
        return pc * x
    return 0


def part1(s):
    cmds = parse(s)
    pc = 1
    x = 1
    signal = 0
    for cmd in cmds:
        # print(pc, x, cmd)
        if len(cmd) == 1:
            pc += 1
            signal += check_signal(x, pc)
        if len(cmd) == 2:
            pc += 1
            signal += check_signal(x, pc)
            pc += 1
            x += int(cmd[1])
            signal += check_signal(x, pc)
    # print(pc, x, "DONE")
    return signal


def check_signal2(sprite, pc):
    return sprite <= pc % 40 < (sprite + 3)


def part2(s):
    cmds = parse(s)
    pc = 0
    x = 0
    crt = set()
    for cmd in cmds:
        if len(cmd) == 1:
            if check_signal2(x, pc):
                crt.add(pc)
            pc += 1
        if len(cmd) == 2:
            if check_signal2(x, pc):
                crt.add(pc)
            pc += 1
            if check_signal2(x, pc):
                crt.add(pc)
            pc += 1
            x += int(cmd[1])
    return crt


def render(crt, fill="."):
    for y in range(6):
        for x in range(40):
            if y * 40 + x in crt:
                print("#", end="")
            else:
                print(fill, end="")
        print()


assert part1(small) == 0
assert part1(example) == 13140
print("Part 1:", part1(task))

render(part2(example))
print()
render(part2(task), fill=" ")
