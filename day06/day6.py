import math


def calculate_ways_to_win(time, distance):
    # We need to press long enough to at least have a chance to reach the
    # required distance
    start = math.ceil(distance / time)
    # The best result is pressing the button for half the maximum time
    # around this point in time the results are mirrored
    end = math.ceil(time / 2)
    won = 0
    for pressed in range(start, end):
        our_distance = pressed * (time - pressed)
        if our_distance > distance:
            won += 1
    won *= 2
    if time % 2 == 0:
        won += 1
    return won


def part1(times, distances):
    ways_to_win = []
    for time, distance in zip(map(int, times), map(int, distances)):
        number_of_wins = calculate_ways_to_win(time, distance)
        ways_to_win.append(number_of_wins)
    return math.prod(ways_to_win)


def part2(times, distances):
    time, distance = int("".join(times)), int("".join(distances))
    return calculate_ways_to_win(time, distance)


if __name__ == "__main__":
    with open("day06/input.txt", "r") as f:
        times, distances = map(lambda line: line.split()[1:], f.read().splitlines())
    p1 = part1(times, distances)
    p2 = part2(times, distances)
    print(p1, p2)
