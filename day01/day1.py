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


def main():
    with open("day01/input.txt", "r") as f:
        input = f.read()

    part1 = 0
    for line in input.splitlines():
        numbers = [char for char in line if str.isnumeric(char)]
        # First learning here. Just add two characters and
        # convert afterward instead of converting them each to int
        # and then adding with multiplication (see part2).
        part1 += int(numbers[0] + numbers[-1])

    # Second learning.
    # Doing a little more work by creating a new list with all digits allows us
    # to not need awkward breaks in the loop.
    part2 = 0
    for line in input.splitlines():
        numbers = []
        for start_idx in range(len(line)):
            if line[start_idx].isnumeric():
                numbers.append(int(line[start_idx]))
                continue
            for test in convert.keys():
                if line.startswith(test, start_idx):
                    numbers.append(convert[test])
                    break
        part2 += numbers[0] * 10 + numbers[-1]

    return part1, part2


if __name__ == "__main__":
    p1, p2 = main()
    print(p1)
    print(p2)
