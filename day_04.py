import aoc

aoc.get_input(4)

with open("input_04.txt", "r") as f:
    task = f.read()


def interesting(s):
    [a,  b] = s.split(',')
    aa = [int(x) for x in a.split('-')]
    bb = [int(x) for x in b.split('-')]
    bina = aa[0] <= bb[0] and aa[1] >= bb[1]
    ainb = aa[0] >= bb[0] and aa[1] <= bb[1]
    if ainb: print(f'{a} in {b}')
    if bina: print(f'{b} in {a}')
    result = bina or ainb
    return result


def sizeit(s):
    [a,  b] = s.split(',')
    aa = [int(x) for x in a.split('-')]
    bb = [int(x) for x in b.split('-')]
    overlap = [x for x in set.intersection(set(range(aa[0], aa[1] + 1)), set(range(bb[0], bb[1] + 1)))]
    return len(overlap)


def task1(inp):
    return sum([1 if interesting(ln) else 0 for ln in inp.splitlines()])


def task2(inp):
    return sum([1 if sizeit(ln) else 0 for ln in inp.splitlines()])


def sanity1():
    assert task1("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""") == 2


def sanity2():
    assert task2("""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""") == 4


sanity1()
sanity2()

print(task1(task))
print(task2(task))



