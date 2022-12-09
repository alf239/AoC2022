import aoc

task = aoc.get_input(9)
example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def parse(ss):
    return [(s.split(" ")[0], int(s.split(" ")[1])) for s in ss.splitlines()]


def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0


def move(c, h):
    hx, hy = h
    if c == "U":
        hy = hy + 1
    elif c == "D":
        hy = hy - 1
    elif c == "L":
        hx = hx - 1
    elif c == "R":
        hx = hx + 1
    return hx, hy


def follow(h, t):
    hx, hy = h
    tx, ty = t
    dx = hx - tx
    dy = hy - ty
    if abs(dx) > 1:
        tx = tx + sign(dx)
        if dy != 0:
            ty = ty + sign(dy)
    elif abs(dy) > 1:
        ty = ty + sign(dy)
        if dx != 0:
            tx = tx + sign(dx)
    return tx, ty


def step(c, h, t):
    h = move(c, h)
    return h, follow(h, t)


def part1(s):
    cs = parse(s)
    h = (0, 0)
    t = (0, 0)
    trail = set()
    trail.add(t)
    for c, n in cs:
        for i in range(n):
            h, t = step(c, h, t)
            trail.add(t)
    return len(trail)


def part2(s):
    cs = parse(s)
    rope = [(0, 0) for _ in range(10)]
    trail = set()
    trail.add(rope[-1])
    for c, n in cs:
        print(c, n)
        for i in range(n):
            rope[0] = move(c, rope[0])
            for j in range(1, len(rope)):
                rope[j] = follow(rope[j - 1], rope[j])
            tail = rope[9]
            trail.add(tail)
    return len(trail)


assert part1(example) == 13
print("Part 1:", part1(task))

# assert part2(example) == 36
print("Part 2:", part2(task))
