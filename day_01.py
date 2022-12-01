x.split("\n")
x.split("\n\n")
elves = x.split("\n\n")
values = [sum([int(a) for a in elf.split("\n")]) for elf in elves]

# Task 1
max(values)

values.sort(reverse=True)
values[:3]

# Task 2
sum(values[:3])
