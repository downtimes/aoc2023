convert = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part1(lines):
    sum = 0
    for line in lines:
        numbers = [char for char in line if str.isnumeric(char)]
        # First learning here. Just add two characters and
        # convert afterward instead of converting them each to int
        # and then adding with multiplication (see part2).
        sum += int(numbers[0] + numbers[-1])
    return sum


def part2(lines):
    # Second learning.
    # Doing a little more work by creating a new list with all digits allows us
    # to not need awkward breaks in the loop.
    sum = 0
    for line in lines:
        numbers = []
        for start_idx in range(len(line)):
            if line[start_idx].isnumeric():
                numbers.append(int(line[start_idx]))
                continue
            for test in convert.keys():
                if line.startswith(test, start_idx):
                    numbers.append(convert[test])
                    break
        sum += numbers[0] * 10 + numbers[-1]
    return sum


if __name__ == "__main__":
    with open("day01/input.txt", "r") as f:
        lines = f.read().splitlines()
    p1 = part1(lines)
    p2 = part2(lines)
    print(p1, p2)
