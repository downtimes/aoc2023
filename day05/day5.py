from itertools import batched, count
import os


def apply_mapping(map, elem):
    for r, adjust in map:
        if elem in r:
            return elem + adjust
    else:
        return elem


def generate_mappings(blocks, reverse):
    maps = []
    for block in blocks:
        mapping = []
        for line in block.splitlines()[1:]:
            dest, source, extend = line.split()
            dest, source, extend = int(dest), int(source), int(extend)
            if reverse:
                mapping.append((range(dest, dest + extend), source - dest))
            else:
                mapping.append((range(source, source + extend), dest - source))
        maps.append(mapping)
    return maps


def part1(blocks):
    seeds = [int(num) for num in blocks[0].split()[1:]]
    maps = generate_mappings(blocks[1:], reverse=False)
    locations = []
    for seed in seeds:
        next = seed
        for mapping in maps:
            next = apply_mapping(mapping, next)
        locations.append(next)
    return min(locations)


# Still brute force!
# Basic idea is to run through locations and calculate backwards if we hit a 
# seed instead of calculating all the locations for all seeds.
# TODO(MA): can we make this faster by eliminating bigger steps?
def part2(blocks):
    seeds = [
        range(int(start), int(start) + int(extend))
        for start, extend in batched(blocks[0].split()[1:], 2)
    ]
    maps = generate_mappings(blocks[1:], reverse=True)
    for loc in count():
        next = loc
        for mapping in reversed(maps):
            next = apply_mapping(mapping, next)
        
        for seed_range in seeds:
            if next in seed_range:
                return loc


if __name__ == "__main__":
    with open("day05/input.txt") as f:
        blocks = f.read().split(2 * "\n")
    p1 = part1(blocks)
    p2 = part2(blocks)
    print(p1, p2)
