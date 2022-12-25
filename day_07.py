#!/usr/bin/env python3

import aoc

task = aoc.get_input(7)
example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def parse(s):
    data = s.splitlines()
    fs = {}
    parent = []
    pwd = fs
    for s in data[1:]:
        if s[0] == "$":
            if s[2] == "c":
                name = s[5:]
                if name == "..":
                    pwd = parent.pop()
                else:
                    parent.append(pwd)
                    _, pwd = pwd[name]
        else:
            [size, name] = s.split(" ")
            if size == "dir":
                pwd[name] = ("dir", {})
            else:
                pwd[name] = ("file", int(size))
    return fs


def walk(fs, collect):
    cnt = 0
    for name, (t, entry) in fs.items():
        if t == "file":
            cnt += entry
        elif t == "dir":
            size = walk(entry, collect)
            collect.append(size)
            cnt += size
    return cnt


def part1(s):
    fs = parse(s)
    sizes = []
    walk(fs, sizes)
    return sum(size for size in sizes if size <= 100000)


def part2(s):
    total = 70000000
    reqd = 30000000
    fs = parse(s)
    sizes = []
    left = total - walk(fs, sizes)
    return min(size for size in sizes if size >= reqd - left)


assert part1(example) == 95437
print("Part 1:", part1(task))

assert part2(example) == 24933642
print("Part 2:", part2(task))
