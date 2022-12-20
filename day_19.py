import dataclasses
from collections import deque
from typing import Tuple

import aoc

task = aoc.get_input(19)
example = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""


@dataclasses.dataclass
class Blueprint:
    id: int
    ore: int
    clay: int
    obsidian: Tuple[int, int]
    geode: Tuple[int, int]

    def __hash__(self) -> int:
        return self.id


def parse_blueprint(s):
    header, body = s.split(": ")
    _, id_s = header.split(" ")
    lines = [s.strip() for s in body.split(".")]
    _, ore_s, _, _, cost_s, unit_s = lines[0].split(" ")
    assert ore_s == "ore"
    assert unit_s == "ore"
    ore = int(cost_s)
    _, clay_s, _, _, cost_s, unit_s = lines[1].split(" ")
    assert clay_s == "clay"
    assert unit_s == "ore"
    clay = int(cost_s)
    _, obsidian_s, _, _, cost1_s, unit1_s, _, cost2_s, unit2_s = lines[2].split(" ")
    assert obsidian_s == "obsidian"
    assert unit1_s == "ore"
    assert unit2_s == "clay"
    obsidian = int(cost1_s), int(cost2_s)
    _, geode_s, _, _, cost1_s, unit1_s, _, cost2_s, unit2_s = lines[3].split(" ")
    assert geode_s == "geode"
    assert unit1_s == "ore"
    assert unit2_s == "obsidian"
    geode = int(cost1_s), int(cost2_s)
    return Blueprint(int(id_s), ore, clay, obsidian, geode)


def parse_input(inp):
    return [parse_blueprint(s) for s in inp.splitlines()]


def max_geodes(bp, t):
    work = deque()
    seen = set()
    baseline = {}
    best = 0

    work.append((t,
                 0, 1,
                 0, 0,
                 0, 0,
                 0, 0))
    while work:
        state = work.pop()
        if state in seen:
            continue
        seen.add(state)
        t, ore, ore_bots, clay, clay_bots, obsidian, obsidian_bots, geode, geode_bots = state
        remaining_time = t - 1

        bl = baseline.setdefault(t, 0)
        if (geode_bots + 1) * t + geode < bl:
            continue
        baseline[t] = max(bl, geode_bots * remaining_time + geode)

        new_ore = ore + ore_bots
        new_clay = clay + clay_bots
        new_obsidian = obsidian + obsidian_bots
        new_geode = geode + geode_bots

        if remaining_time == 0:
            best = max(new_geode, best)
            continue

        if ore >= bp.geode[0] and obsidian >= bp.geode[1]:
            work.append((remaining_time,
                         new_ore - bp.geode[0], ore_bots,
                         new_clay, clay_bots,
                         new_obsidian - bp.geode[1], obsidian_bots,
                         new_geode, geode_bots + 1))
            continue  # we always build geode bots if we can

        if new_ore < 22 or new_clay < 22 or new_obsidian < 22 or remaining_time > 2:
            work.append((remaining_time,
                         new_ore, ore_bots,
                         new_clay, clay_bots,
                         new_obsidian, obsidian_bots,
                         new_geode, geode_bots))

        if ore >= bp.ore:
            work.append((remaining_time,
                         new_ore - bp.ore, ore_bots + 1,
                         new_clay, clay_bots,
                         new_obsidian, obsidian_bots,
                         new_geode, geode_bots))

        if ore >= bp.clay:
            work.append((remaining_time,
                         new_ore - bp.clay, ore_bots,
                         new_clay, clay_bots + 1,
                         new_obsidian, obsidian_bots,
                         new_geode, geode_bots))

        if ore >= bp.obsidian[0] and clay >= bp.obsidian[1]:
            work.append((remaining_time,
                         new_ore - bp.obsidian[0], ore_bots,
                         new_clay - bp.obsidian[1], clay_bots,
                         new_obsidian, obsidian_bots + 1,
                         new_geode, geode_bots))

    return best


def part1(inp):
    blueprints = parse_input(inp)
    qs = [bp.id * max_geodes(bp, 24) for bp in blueprints]
    print(qs)
    return sum(qs)


N2 = 32


def part2(inp):
    blueprints = parse_input(inp)[:3]
    qs = [max_geodes(bp, N2) for bp in blueprints]
    print(qs)
    return qs[0] * qs[1] * qs[2]


assert part1(example) == 33
print("Part 1:", part1(task))

assert max_geodes(parse_input(example)[0], N2) == 56
assert max_geodes(parse_input(example)[1], N2) == 62
print("Part 2:", part2(task))
