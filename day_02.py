rounds = x.split("\n")
score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}


def outcome(s):
    elf = score[s[0]]
    you = score[s[2]]
    if elf == you: return 3
    if (elf + 1) % 3 == you % 3: return 6
    return 0


sum([score[s[2]] + outcome(s) for s in rounds])


def full_score2(s):
    elf = score[s[0]]
    you = s[2]
    if you == 'X': return 0 + (elf + 1) % 3 + 1
    if you == 'Y': return 3 + elf
    return 6 + elf % 3 + 1


sum([full_score2(s) for s in rounds])
