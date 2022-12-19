import dataclasses
from typing import Tuple
from functools import cache

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


@cache
def max_geodes(bp, ore, ore_bots, clay, clay_bots, obsidian, obsidian_bots, t):
    if t == 0:
        return 0
    new_ore = ore + ore_bots
    new_clay = clay + clay_bots
    new_obsidian = obsidian + obsidian_bots
    remaining_time = t - 1
    if ore >= bp.geode[0] and obsidian >= bp.geode[1]:
        return (remaining_time +
                max_geodes(bp,
                           new_ore - bp.geode[0], ore_bots,
                           new_clay, clay_bots,
                           new_obsidian - bp.geode[1], obsidian_bots,
                           remaining_time))
    best = 0
    if ore >= bp.obsidian[0] and clay >= bp.obsidian[1]:
        best = max(best,
                   max_geodes(bp,
                              new_ore - bp.obsidian[0], ore_bots,
                              new_clay - bp.obsidian[1], clay_bots,
                              new_obsidian, obsidian_bots + 1,
                              remaining_time))

    if ore >= bp.clay:
        best = max(best,
                   max_geodes(bp,
                              new_ore - bp.clay, ore_bots,
                              new_clay, clay_bots + 1,
                              new_obsidian, obsidian_bots,
                              remaining_time))

    if ore >= bp.ore:
        best = max(best,
                   max_geodes(bp,
                              new_ore - bp.ore, ore_bots + 1,
                              new_clay, clay_bots,
                              new_obsidian, obsidian_bots,
                              remaining_time))

    best = max(best, max_geodes(bp,
                                new_ore, ore_bots,
                                new_clay, clay_bots,
                                new_obsidian, obsidian_bots,
                                remaining_time))

    return best


def max_geodes_facade(bp, n):
    return max_geodes(bp, 0, 1, 0, 0, 0, 0, n)


def part1(inp):
    blueprints = parse_input(inp)
    qs = [bp.id * max_geodes_facade(bp, 24) for bp in blueprints]
    print(qs)
    return sum(qs)


def part2(inp):
    blueprints = parse_input(inp)[:3]
    qs = [max_geodes_facade(bp, 36) for bp in blueprints]
    print(qs)
    return sum(qs)


# assert part1(example) == 33
# print("Part 1:", part1(task))

# assert part2(example) == 62
print("Part 2:", part2(task))
