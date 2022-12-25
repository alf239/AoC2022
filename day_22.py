#!/usr/bin/env python3

import aoc

task = aoc.get_input(22)
example = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""

FACING = [(1, 0), (0, 1), (-1, 0), (0, -1)]
FACING_ICON = '>v<^'


def parse(inp):
    [a, b] = inp.split("\n\n")
    commands = b.splitlines()[0]
    return a.splitlines(), commands


def falling_out(m, x, y):
    return x < 0 or y < 0 or y >= len(m) or x >= len(m[y]) or m[y][x] == ' '


def obstacle(m, x, y):
    return m[y][x] == '#'


def part1(inp, trace=False):
    map, cs = parse(inp)
    nr = 0
    commands = []
    for c in cs:
        if '0' <= c <= '9':
            nr = nr * 10 + int(c)
            continue
        if nr != 0:
            commands.append(('move', nr))
            nr = 0
        commands.append(('turn', c))
    if nr != 0:
        commands.append(('move', nr))

    row, facing = 0, 0
    col = min(c for c in range(len(map[row])) if map[row][c] == '.')

    report = [[c for c in s] for s in map]
    report[row][col] = 'S'
    for cmd, par in commands:
        if trace:
            print(col, row, facing)
            print(cmd, par)
        if cmd == 'turn':
            if par == 'R':
                facing = (facing + 1) % 4
            else:
                facing = (facing - 1) % 4
            report[row][col] = FACING_ICON[facing]
        elif cmd == 'move':
            for n in range(par):
                if facing == 0 or facing == 2:
                    new_col = col + FACING[facing][0]
                    new_row = row
                    if falling_out(map, new_col, new_row):
                        if trace:
                            print(f"wrapping at step {n}")
                        if FACING[facing][0] > 0:
                            new_col = min(c for c in range(len(map[row])) if map[row][c] != ' ')
                        else:
                            new_col = max(c for c in range(len(map[row])) if map[row][c] != ' ')
                else:
                    new_col = col
                    new_row = row + FACING[facing][1]
                    if falling_out(map, new_col, new_row):
                        if trace:
                            print(f"wrapping at step {n}")
                        if FACING[facing][1] > 0:
                            new_row = min(r for r in range(len(map)) if col < len(map[r]) and map[r][col] != ' ')
                        else:
                            new_row = max(r for r in range(len(map)) if col < len(map[r]) and map[r][col] != ' ')
                if obstacle(map, new_col, new_row):
                    if trace:
                        print(f"hit the wall at step {n}")
                    break
                col = new_col
                row = new_row
                report[row][col] = FACING_ICON[facing]
    if trace:
        for s in report:
            print(''.join(s))
        print('finish:', col, row, facing)
    return 1000 * (row + 1) + 4 * (col + 1) + facing


def part2(inp, transitions, m, trace=False):
    map, cs = parse(inp)
    nr = 0
    commands = []
    for c in cs:
        if '0' <= c <= '9':
            nr = nr * 10 + int(c)
            continue
        if nr != 0:
            commands.append(('move', nr))
            nr = 0
        commands.append(('turn', c))
    if nr != 0:
        commands.append(('move', nr))

    row, facing = 0, 0
    col = min(c for c in range(len(map[row])) if map[row][c] == '.')

    report = [[c for c in s] for s in map]
    report[row][col] = 'S'
    for cmd, par in commands:
        if trace:
            print(col, row, facing)
            print(cmd, par)
        if cmd == 'turn':
            if par == 'R':
                facing = (facing + 1) % 4
            else:
                facing = (facing - 1) % 4
            report[row][col] = FACING_ICON[facing]
        elif cmd == 'move':
            for n in range(par):
                new_facing = facing
                if facing == 0:
                    new_col = col + FACING[facing][0]
                    new_row = row
                    if falling_out(map, new_col, new_row):
                        mx, my, new_facing = new_face(m, transitions, col, row, facing, n, trace)
                        if new_facing == 0:
                            new_col = m * mx
                            new_row = m * my + row % m
                        elif new_facing == 1:
                            new_col = m * mx + m - 1 - row % m
                            new_row = m * my
                        elif new_facing == 2:
                            new_col = m * mx + m - 1
                            new_row = m * my + (m - 1 - row % m)
                        else:
                            new_col = m * mx + row % m
                            new_row = m * my + m - 1
                elif facing == 2:
                    new_col = col + FACING[facing][0]
                    new_row = row
                    if falling_out(map, new_col, new_row):
                        mx, my, new_facing = new_face(m, transitions, col, row, facing, n, trace)
                        if new_facing == 0:
                            new_col = m * mx
                            new_row = m * my + m - 1 - row % m
                        elif new_facing == 1:
                            new_col = m * mx + row % m
                            new_row = m * my
                        elif new_facing == 2:
                            new_col = m * mx + m - 1
                            new_row = m * my + row % m
                        else:
                            new_col = m * mx + m - 1 - row % m
                            new_row = m * my + m - 1
                elif facing == 1:
                    new_col = col
                    new_row = row + FACING[facing][1]
                    if falling_out(map, new_col, new_row):
                        mx, my, new_facing = new_face(m, transitions, col, row, facing, n, trace)
                        if new_facing == 0:
                            new_col = m * mx
                            new_row = m * my + m - 1 - col % m
                        elif new_facing == 1:
                            new_col = m * mx + col % m
                            new_row = m * my
                        elif new_facing == 2:
                            new_col = m * mx + m - 1
                            new_row = m * my + col % m
                        else:
                            new_col = m * mx + m - 1 - col % m
                            new_row = m * my + m - 1
                else:
                    new_col = col
                    new_row = row + FACING[facing][1]
                    if falling_out(map, new_col, new_row):
                        mx, my, new_facing = new_face(m, transitions, col, row, facing, n, trace)
                        if new_facing == 0:
                            new_col = m * mx
                            new_row = m * my + col % m
                        elif new_facing == 1:
                            new_col = m * mx + m - 1 - col % m
                            new_row = m * my
                        elif new_facing == 2:
                            new_col = m * mx + m - 1
                            new_row = m * my + m - 1 - col % m
                        else:
                            new_col = m * mx + col % m
                            new_row = m * my + m - 1

                if trace:
                    print(f"trying {(new_col, new_row, new_facing)}")
                if obstacle(map, new_col, new_row):
                    if trace:
                        print(f"hit the wall at step {n}")
                    break
                col = new_col
                row = new_row
                facing = new_facing
                report[row][col] = FACING_ICON[facing]
    if trace:
        for s in report:
            print(''.join(s))
        print('finish:', col, row, facing)
    return 1000 * (row + 1) + 4 * (col + 1) + facing


def new_face(m, transitions, col, row, facing, n, trace):
    part = (col // m, row // m)
    wrap = transitions[part][facing]
    if trace:
        print(f"wrapping at step {n}: {wrap} for {(col, row, facing)}")
    return wrap


assert part1(example) == 6032
print("Part 1:", part1(task))

example_transitions = {
    (2, 0): [(3, 2, 2), None, (1, 1, 1), (0, 1, 1)],
    (0, 1): [None, (2, 2, 3), (3, 2, 3), (2, 0, 1)],
    (1, 1): [None, (2, 2, 0), None, (2, 0, 0)],
    (2, 1): [(3, 2, 1), None, None, None],
    (2, 2): [None, (0, 1, 3), (1, 1, 3), None],
    (3, 2): [(2, 0, 2), (0, 1, 0), None, (2, 1, 2)]
}

task_transitions = {
    (1, 0): [None, None, (0, 2, 0), (0, 3, 0)],
    (2, 0): [(1, 2, 2), (1, 1, 2), None, (0, 3, 3)],
    (1, 1): [(2, 0, 3), None, (0, 2, 1), None],
    (0, 2): [None, None, (1, 0, 0), (1, 1, 0)],
    (1, 2): [(2, 0, 2), (0, 3, 2), None, None],
    (0, 3): [(1, 2, 3), (2, 0, 1), (1, 0, 1), None]
}

# assert part2(example, example_transitions, m=4) == 5031
print("Part 2:", part2(task, task_transitions, m=50, trace=True))
