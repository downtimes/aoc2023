import math


# find beginning and end of the number
def extend_of_number(line, col):
    begin = col
    while 0 < begin and line[begin].isdecimal():
        begin -= 1
    if not line[begin].isdecimal():
        begin += 1

    end = col
    while end < len(line) and line[end].isdecimal():
        end += 1

    return begin, end


def part1(lines):
    sum = 0
    # This set is additional information to remember which numbers we already
    # counted, since python strings are immutable and we can't just replace
    # already extracted numbers by replacing them with '.'
    extracted = set()
    for row, line in enumerate(lines):
        for col, character in enumerate(line):
            if character.isdecimal() or character == ".":
                continue
            else:
                # We found a symbol so check all positions around the symbol
                # for any signs of a number. Limit to positions inside grid
                positions = [
                    (r, c)
                    for r in range(row - 1, row + 2)
                    for c in range(col - 1, col + 2)
                    if 0 <= r < len(lines) and 0 <= c < len(line)
                ]
                # Big learning: don't ever reuse a name from a for loop since
                # we actually modify the value of the for loop when writing
                # to the variable.
                for r, c in positions:
                    test_line = lines[r]
                    if test_line[c].isdecimal() and (r, c) not in extracted:
                        begin, end = extend_of_number(test_line, c)
                        for num_index in range(begin, end):
                            extracted.add((r, num_index))
                        sum += int(test_line[begin:end])
    return sum


def part2(lines):
    sum = 0
    extracted = set()
    for row, line in enumerate(lines):
        for col, character in enumerate(line):
            if character == "*":
                # We found a gear so check all positions around the symbol
                # for any signs of a number. Limit to positions inside grid
                positions = [
                    (r, c)
                    for r in range(row - 1, row + 2)
                    for c in range(col - 1, col + 2)
                    if 0 <= r < len(lines) and 0 <= c < len(line)
                ]
                numbers = []
                for r, c in positions:
                    test_line = lines[r]
                    if test_line[c].isdecimal() and (r, c) not in extracted:
                        begin, end = extend_of_number(test_line, c)
                        for num_index in range(begin, end):
                            extracted.add((r, num_index))
                        numbers.append(int(test_line[begin:end]))
                # only add to sum if we have exactly two numbers near the gear
                if len(numbers) == 2:
                    sum += math.prod(numbers)
    return sum


if __name__ == "__main__":
    with open("./day03/input.txt", "r+") as f:
        lines = f.read().splitlines()
    p1 = part1(lines)
    p2 = part2(lines)
    print(p1)
    print(p2)
