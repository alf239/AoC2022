import aoc

task = aoc.get_input(11)
example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


def parse(s):
    cmds = [s1.split(" ") for s1 in s.splitlines()]
    monkeys = []
    monkey = {}
    i = 0
    for cmd in cmds:
        # print(cmd)
        if len(cmd) <= 1:
            monkeys.append(monkey)
        elif cmd[0] == "Monkey":
            monkey = {"Turns": 0, "Nr": i}
            i = i + 1
        elif cmd[2] == "Starting":
            monkey["Items"] = [int(x.split(",")[0]) for x in cmd[4:]]
        elif cmd[2] == "Operation:":
            monkey["Op"] = " ".join(cmd[5:])
        elif cmd[2] == "Test:":
            monkey["Test"] = int(cmd[5])
        elif cmd[5] == "true:":
            monkey["True"] = int(cmd[9])
        elif cmd[5] == "false:":
            monkey["False"] = int(cmd[9])
    monkeys.append(monkey)
    return monkeys


def monkey_business(monkeys):
    activity = [mn["Turns"] for mn in monkeys]
    activity.sort(reverse=True)
    return activity[0] * activity[1]


def part1(s):
    monkeys = parse(s)

    for i in range(20):
        for m in monkeys:
            for item in m["Items"]:
                m["Turns"] = m["Turns"] + 1
                worry = eval(m["Op"], {}, {"old": item}) // 3
                target = m[str((worry % m["Test"]) == 0)]
                pass_to = monkeys[target]
                pass_to["Items"].append(worry)
            m["Items"] = []

    return monkey_business(monkeys)


def part2(s):
    monkeys = parse(s)
    modulo = 1
    for m in monkeys:
        modulo *= m["Test"]

    for i in range(10000):
        for m in monkeys:
            for item in m["Items"]:
                m["Turns"] = m["Turns"] + 1
                worry = eval(m["Op"], {}, {"old": item}) % modulo
                target = m[str((worry % m["Test"]) == 0)]
                pass_to = monkeys[target]
                pass_to["Items"].append(worry)
            m["Items"] = []

    return monkey_business(monkeys)


assert part1(example) == 10605
print("Part 1:", part1(task))

assert part2(example) == 2713310158
print("Part 2:", part2(task))
