from collections import defaultdict


def part1(cards):
    sum = 0
    for card in cards:
        (haves, wants) = card.split(":", 1)[1].split("|", 1)
        haves = {int(number) for number in haves.split()}
        wants = {int(number) for number in wants.split()}
        matching = len(haves & wants)
        sum += 2 ** (matching - 1) if matching > 0 else 0
    return sum


def part2(cards):
    # First learning: better than using defaultdict.
    # 0 index is not relevant since we are
    # only interested in the number of cards and not their correct id.
    card_count = [1] * len(cards)
    for card_number, card in enumerate(cards):
        (haves, wants) = card.split(":", 1)[1].split("|", 1)
        haves = {int(number) for number in haves.split()}
        wants = {int(number) for number in wants.split()}
        matching = len(haves & wants)
        cards_to_add = [
            card_number + i
            for i in range(1, matching + 1)
            if card_number + i < len(cards)
        ]
        for card in cards_to_add:
            card_count[card] += card_count[card_number]
    return sum(card_count)


if __name__ == "__main__":
    with open("day04/input.txt", "r") as f:
        cards = f.read().rstrip().splitlines()
    p1 = part1(cards)
    p2 = part2(cards)
    print(p1, p2)
