def value(c):
    if c < 'a':
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def the_only(first, second):
    return [c for c in set.intersection(set(first), set(second))][0]


def item(s):
    if s == "": return 0

    h = len(s) // 2
    first = s[:h]
    second = s[-h:]
    common = the_only(first, second)

    return value(common)


def the_only_2(first, second, third):
    return [c for c in set.intersection(set.intersection(set(first), set(second)), set(third))][0]


with open("input_03.txt", "r") as f:
    task = f.read().splitlines(keepends=False)

scores = [item(s) for s in task]

print(sum(scores))

chunk_size = 3
task2 = 0
for i in range(0, len(task), chunk_size):
    chunk = task[i:i+chunk_size]
    task2 += value(the_only_2(chunk[0], chunk[1], chunk[2]))

print(task2)



