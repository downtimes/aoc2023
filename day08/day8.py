from itertools import cycle
import math
import re


def part1(instructions, maps):
    current = "AAA"
    end = "ZZZ"
    mapping = convert(maps)
    # First learning: cycle from itertools!
    # Second learning: we can still use step after the for loop with enumerate
    for step, ins in enumerate(cycle(instructions), start=1):
        current = mapping[current][0] if ins == "L" else mapping[current][1]
        if current == end:
            break
    return step


def part2(instructions, maps):
    mapping = convert(maps)
    current_pos = [s for s in mapping.keys() if s[2] == "A"]
    num_starts = len(current_pos)
    # Apparently every start only ever hits one distinct end, was found experimentally.
    # Every run loops around after hitting the end. Therefore, we just get all the
    # steps to the end hits and calculate the least common multiple
    end_steps = []
    for step, ins in enumerate(cycle(instructions), start=1):
        new_pos = []
        for c in current_pos:
            new = mapping[c][0] if ins == "L" else mapping[c][1]
            if new[2] == "Z":
                end_steps.append(step)
            else:
                new_pos.append(new)
        current_pos = new_pos
        if len(end_steps) >= num_starts:
            break
    return math.lcm(*end_steps)


def convert(maps):
    mapping = {}
    for m in maps:
        # Third learning: regex strings should be marked r" (raw) if we need to 
        #                 escape () for example.
        match = re.search(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", m)
        node, left, right = match.groups()
        mapping[node] = (left, right)
    return mapping


if __name__ == "__main__":
    with open("day08/input.txt") as f:
        lines = f.read().splitlines()
        instructions, maps = lines[0], lines[2:]
    p1 = part1(instructions, maps)
    p2 = part2(instructions, maps)
    print(p1, p2)
