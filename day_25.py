from itertools import zip_longest

import aoc

task = aoc.get_input(25)
example = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

VALUE = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
DIGITS = '=-012'


def to_decimal(s):
    n = 0
    for c in s:
        n = n * 5 + VALUE[c]
    return n


def to_pentary(n):
    pentary = []
    while n != 0:
        pentary.append(n % 5)
        n //= 5
    pentary.reverse()
    return ''.join(str(d) for d in pentary)


def pentary_sum(a, b):
    da = [int(c) for c in a]
    db = [int(c) for c in b]
    da.reverse()
    db.reverse()
    carry = 0
    result = []
    for d1, d2 in zip_longest(da, db, fillvalue=0):
        dd = d1 + d2 + carry
        carry = dd // 5
        dd %= 5
        result.append(dd)
    if carry > 0:
        result.append(carry)
    result.reverse()
    return ''.join(str(d) for d in result)


def pentary_sub(a, b):
    da = [int(c) for c in a]
    db = [int(c) for c in b]
    da.reverse()
    db.reverse()
    result = []
    for d1, d2 in zip_longest(da, db, fillvalue=0):
        dd = d1 - d2
        result.append(dd)
    result.reverse()
    return ''.join(DIGITS[d + 2] for d in result)


def to_snafu(d):
    pentary = to_pentary(d)
    corrector = '2' * (len(pentary) - 1)
    adjusted = pentary_sum(pentary, corrector)
    return pentary_sub(adjusted, corrector)


def part1(inp):
    return to_snafu(sum(to_decimal(s) for s in inp.splitlines()))


assert part1(example) == "2=-1=0"
print("Part 1:", part1(task))
