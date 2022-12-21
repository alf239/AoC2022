import aoc

task = aoc.get_input(21)
example = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


def parse_monkey(s):
    [name, code] = s.split(": ")
    terms = code.split(" ")
    if len(terms) == 1:
        return name, int(terms[0]), set()
    return name, code, {terms[0], terms[2]}


def part1(inp):
    ms = [parse_monkey(s) for s in inp.splitlines()]

    known = {m[0]: m[1] for m in ms if len(m[2]) == 0}
    unknown = {m[0]: (m[1], m[2]) for m in ms if len(m[2]) > 0}

    while unknown:
        for name, m in unknown.items():
            code, deps = m
            if not all(n in known for n in deps):
                continue
            value = eval(code, known)
            known[name] = value
            del unknown[name]
            break

    return known["root"]



def part2(inp):
    ms = [parse_monkey(s) for s in inp.splitlines()]

    known = {m[0]: m[1] for m in ms if len(m[2]) == 0}
    unknown = {m[0]: (m[1], m[2]) for m in ms if len(m[2]) > 0}

    del known["humn"]
    [a, b] = unknown["root"][1]

    while a in unknown and b in unknown:
        for name, m in unknown.items():
            code, deps = m
            if not all(n in known for n in deps):
                continue
            value = eval(code, known)
            known[name] = value
            del unknown[name]
            break

    if a in known:
        value = known[a]
        goal = b
    else:
        value = known[b]
        goal = a

    while goal != 'humn':
        code, deps = unknown[goal]
        print(value, '=', code)
        [x, op, y] = code.split(' ')
        if x in known:
            xv = known[x]
            goal = y
            if op == '+':
                value = value - xv
            elif op == '-':
                value = xv - value
            elif op == '/':
                value = xv / value
            elif op == '*':
                value = value / xv
        else:
            yv = known[y]
            goal = x
            if op == '+':
                value = value - yv
            elif op == '-':
                value = yv + value
            elif op == '/':
                value = yv * value
            elif op == '*':
                value = value / yv

    return value


assert part1(example) == 152
print("Part 1:", part1(task))

assert part2(example) == 301.0
print("Part 2:", part2(task))
