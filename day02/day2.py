import math


def possible(selection):
    BLUE_LIMIT = 14
    GREEN_LIMIT = 13
    RED_LIMIT = 12
    return (
        selection.get("green", 0) <= GREEN_LIMIT
        and selection.get("blue", 0) <= BLUE_LIMIT
        and selection.get("red", 0) <= RED_LIMIT
    )


# Instead of handcrafting our input parser it is probably better to embrace
# regular expressions for most of the problems.
def transform_input(lines: list[str]):
    transformed = []
    for line in lines:
        elems = line[line.index(":") + 1 :].split(";")
        selections = []
        for selection in elems:
            cubes = [str.strip(cube) for cube in selection.split(",")]
            one_selection = {}
            for cube in cubes:
                cube_info = cube.split(maxsplit=1)
                one_selection[cube_info[1]] = int(cube_info[0])
            selections.append(one_selection)
        transformed.append(selections)
    return transformed


def part1(lines: list[str]):
    transformed = transform_input(lines)
    sum = 0
    # First learning: we can manipulate the start index of enumerate!
    for i, selections in enumerate(transformed, start=1):
        if all(map(possible, selections)):
            sum += i

    return sum


def part2(lines: list[str]):
    transformed = transform_input(lines)
    sum = 0
    for selections in transformed:
        # Second learning: better to prefill data instead of handling corner
        # cases.
        maximum = {"red": 0, "green": 0, "blue": 0}
        for selection in selections:
            for k, v in selection.items():
                maximum[k] = max(v, maximum[k])
        # Third learning: math.prod to calculate product over whole list.
        sum += math.prod(maximum.values())

    return sum


if __name__ == "__main__":
    with open("day02/input.txt", "r") as file:
        lines = file.read().splitlines()
    p1 = part1(lines)
    p2 = part2(lines)
    print(p1, p2)
