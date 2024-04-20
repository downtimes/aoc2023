from collections import Counter


NORMAL_ORDER = "23456789TJQKA"
JOKER_ORDER = "J23456789TQKA"

FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
PAIR = 2
NOTHING = 1


def part1(hands):
    s = sorted(hands, key=map_to_value)
    sum = 0
    for rank, (_, val) in enumerate(s, start=1):
        sum += rank * val
    return sum


def part2(hands):
    s = sorted(hands, key=map_to_value_joker)
    sum = 0
    for rank, (_, val) in enumerate(s, start=1):
        sum += rank * val
    return sum


def map_to_value_joker(entry):
    hand = entry[0]
    without_joker = [c for c in hand if c != "J"]
    rank = rank_of_hand(without_joker, len(hand) - len(without_joker))
    return (rank, [JOKER_ORDER.index(c) for c in hand])


def map_to_value(entry):
    h = entry[0]
    rank = rank_of_hand(h, 0)
    return (rank, [NORMAL_ORDER.index(c) for c in h])


# Learning number 1: Counter is a useful collection! Remember it exists.
def rank_of_hand(hand, num_jokers):
    if num_jokers == 5:
        return FIVE_KIND

    clusters = Counter(hand).most_common(2)
    highest = clusters[0][1] + num_jokers
    if highest == 5:
        return FIVE_KIND

    second_highest = clusters[1][1]
    if highest == 4:
        return FOUR_KIND
    if highest == 3 and second_highest == 2:
        return FULL_HOUSE
    if highest == 3:
        return THREE_KIND
    if highest == 2 and second_highest == 2:
        return TWO_PAIR
    if highest == 2:
        return PAIR
    return NOTHING


def convert_into_hand(line: str):
    s = line.split()
    return (s[0], int(s[1]))


if __name__ == "__main__":
    with open("day07/input.txt") as f:
        lines = f.read().splitlines()
        hands = [convert_into_hand(l) for l in lines]
    p1 = part1(hands)
    p2 = part2(hands)
    print(p1, p2)
