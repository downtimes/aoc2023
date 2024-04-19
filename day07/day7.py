from functools import cmp_to_key

FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
PAIR = 2
NOTHING = 1


def part1(hands):
    s = sorted(hands, key=cmp_to_key(compare))
    sum = 0
    for i, h in enumerate(s, start=1):
        sum += i * h[1]
    return sum


def part2(hands):
    s = sorted(hands, key=cmp_to_key(compare_wicked))
    sum = 0
    for i, h in enumerate(s, start=1):
        sum += i * h[1]
    return sum


def count_same(s):
    res = []
    run = 1
    if not len(s):
        return res
    last = s[0]

    for e in s[1:]:
        if e == last:
            run += 1
        else:
            res.append(run)
            run = 1
        last = e
    res.append(run)
    return res


def compare_wicked(h1, h2):
    filtered1 = [c for c in h1[0] if c != "J"]
    filtered2 = [c for c in h2[0] if c != "J"]
    r1 = rank_of_hand(filtered1, len(h1[0]) - len(filtered1))
    r2 = rank_of_hand(filtered2, len(h2[0]) - len(filtered2))
    if r1 > r2:
        return 1
    if r1 < r2:
        return -1

    for f, s in zip(h1[0], h2[0]):
        v1 = value_of_card_alt(f)
        v2 = value_of_card_alt(s)
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
    return 0


def rank_of_hand(h, num_j):
    if num_j == 5:
        return FIVE_KIND

    s = sorted(h)
    counted = count_same(s)
    counted.sort(reverse=True)
    highest = counted[0] + num_j
    if highest == 5:
        return FIVE_KIND

    next = counted[1]
    if highest == 4:
        return FOUR_KIND
    if highest == 3 and next == 2:
        return FULL_HOUSE
    if highest == 3:
        return THREE_KIND
    if highest == 2 and next == 2:
        return TWO_PAIR
    if highest == 2:
        return PAIR
    return NOTHING


# instead of compare function, a key function would be better
def compare(h1, h2):
    r1, r2 = rank_of_hand(h1[0], 0), rank_of_hand(h2[0], 0)
    if r1 > r2:
        return 1
    if r1 < r2:
        return -1

    for f, s in zip(h1[0], h2[0]):
        v1 = value_of_card(f)
        v2 = value_of_card(s)
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
    return 0


def value_of_card(c):
    CARDS = "23456789TJQKA"
    return CARDS.index(c)


def value_of_card_alt(c):
    CARDS = "J23456789TQKA"
    return CARDS.index(c)


def map_to_hand(line):
    s = line.split()
    return (s[0], int(s[1]))


if __name__ == "__main__":
    with open("day07/input.txt") as f:
        lines = f.read().splitlines()
        hands = [map_to_hand(l) for l in lines]
    p1 = part1(hands)
    p2 = part2(hands)
    print(p1, p2)
