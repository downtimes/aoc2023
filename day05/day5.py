from itertools import batched, count


# A list of the new ranges in the appropriate level is generated if an overlap is found.
# If the generated list is empty, no overlap of the range and mapping could be found
def calculate_overlap(mapping, input, adjust, level):
    result = []
    overlap_start = input.start
    overlap_end = input.stop
    if input.stop <= mapping.start or input.start >= mapping.stop: 
        return result
    # Keep the non overlapping area in the same level to check against
    # other mappings on this level
    if input.start < mapping.start:
        result.append((range(input.start, mapping.start), level))
        overlap_start = mapping.start
    if mapping.stop < input.stop:
        result.append((range(mapping.stop, input.stop), level))
        overlap_end = mapping.stop
    # The overlapped area is mapped and will next be tested against the lower level
    result.append((range(overlap_start + adjust, overlap_end + adjust), level + 1))
    return result


def apply_mapping(map, elem):
    for r, adjust in map:
        if elem in r:
            return elem + adjust
    else:
        return elem


def generate_mappings(blocks):
    maps = []
    for block in blocks:
        mapping = []
        for line in block.splitlines()[1:]:
            dest, source, extend = map(int, line.split())
            mapping.append((range(source, source + extend), dest - source))
        maps.append(mapping)
    return maps


def part1(blocks):
    seeds = [int(num) for num in blocks[0].split()[1:]]
    maps = generate_mappings(blocks[1:])
    locations = []
    for seed in seeds:
        next = seed
        for mapping in maps:
            next = apply_mapping(mapping, next)
        locations.append(next)
    return min(locations)


# Basic idea is to match whole ranges against the mappings and move ranges
# through the levels instead of single seeds. When we have a location range we
# can simply take the first element of the range as minimum.
#
# After we do this for all ranges, we have a list of minima locations for them
# and simply need to select the lowest as our result.
def part2(blocks):
    queue = [
        (range(start, start + extend), 0)
        for start, extend in batched(map(int, blocks[0].split()[1:]), 2)
    ]
    maps = generate_mappings(blocks[1:])

    ranges_min = []
    while queue:
        input, level = queue.pop()
        if level == len(maps):
            ranges_min.append(input.start)
            continue

        for mapping, adjust in maps[level]:
            new_ranges = calculate_overlap(mapping, input, adjust, level)
            if new_ranges:
                queue.extend(new_ranges)
                # The range we were currently processing is completely split
                # up into new ranges now. Therefore we can stop looking for
                # mappings for it and continue with the next element from our queue.
                break
        else:
            # The range had zero overlap with any of the mappings so move to 
            # next level untouched
            queue.append((input, level + 1))
    return min(ranges_min)


if __name__ == "__main__":
    with open("day05/input.txt", "r") as f:
        blocks = f.read().split(2 * "\n")
    p1 = part1(blocks)
    p2 = part2(blocks)
    print(p1, p2)
