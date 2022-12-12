import aoc

DEBUG = False
BARRIER = '|'

task = aoc.get_input(12)
example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def read(m, x, y):
    if x < 0:
        return BARRIER
    if y < 0:
        return BARRIER
    if x >= len(m[0]):
        return BARRIER
    if y >= len(m):
        return BARRIER
    signal = m[y][x]
    if signal == 'S':
        return 'a'
    if signal == 'E':
        return 'z'
    return signal


def start(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 'S':
                return x, y
    raise Exception("Cannot start")


def finish(m):
    for y in range(len(m)):
        for x in range(len(m[0])):
            if m[y][x] == 'E':
                return x, y
    raise Exception("Cannot start")


def show_path(m, visited):
    if not DEBUG:
        return
    for y in range(len(m)):
        for x in range(len(m[0])):
            if (x, y) in visited:
                print(f'{visited[(x, y)]:4d}', end="")
            else:
                print("    ", end="")
        print()


def part1(ss):
    m = [[c for c in s] for s in ss.splitlines()]
    visited = {}
    work = []
    x0, y0 = start(m)
    xz, yz = finish(m)
    work[:0] = [(x0, y0, 0)]
    while work:
        x, y, cnt = work.pop()
        if (x, y) in visited:
            continue
        visited[(x, y)] = cnt
        signal = read(m, x, y)
        if (x, y) == (xz, yz):
            show_path(m, visited)
            return cnt
        if signal == 'S':
            signal = 'a'
        step = cnt + 1
        if ord(read(m, x + 1, y)) <= ord(signal) + 1:
            work[:0] = [(x + 1, y, step)]
        if ord(read(m, x - 1, y)) <= ord(signal) + 1:
            work[:0] = [(x - 1, y, step)]
        if ord(read(m, x, y + 1)) <= ord(signal) + 1:
            work[:0] = [(x, y + 1, step)]
        if ord(read(m, x, y - 1)) <= ord(signal) + 1:
            work[:0] = [(x, y - 1, step)]

    raise Exception("Out of work, no cigar")


def part2(ss):
    m = [[c for c in s] for s in ss.splitlines()]
    visited = {}
    work = []
    x0, y0 = finish(m)
    work[:0] = [(x0, y0, 0)]
    while work:
        x, y, cnt = work.pop()
        if (x, y) in visited:
            continue
        visited[(x, y)] = cnt
        signal = read(m, x, y)
        if signal == 'a':
            show_path(m, visited)
            return cnt
        if signal == 'S':
            signal = 'a'
        step = cnt + 1
        if ord(read(m, x + 1, y)) >= ord(signal) - 1:
            work[:0] = [(x + 1, y, step)]
        if ord(read(m, x - 1, y)) >= ord(signal) - 1:
            work[:0] = [(x - 1, y, step)]
        if ord(read(m, x, y + 1)) >= ord(signal) - 1:
            work[:0] = [(x, y + 1, step)]
        if ord(read(m, x, y - 1)) >= ord(signal) - 1:
            work[:0] = [(x, y - 1, step)]

    raise Exception("Out of work, no cigar")


assert part1(example) == 31
print("Part 1:", part1(task))

assert part2(example) == 29
print("Part 2:", part2(task))
