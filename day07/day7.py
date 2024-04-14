# map to relative strength by applying function
# value of hand = sum(for all cards: (6 - card_position) * card_value)
# - with card_value = 2 -> 1, ... A -> 12
# overall_value = Five of a kind 6 * 252 + hand_value, ... High card 0 * 252 + hand_value
# - 252 from sum(range(7)) * 12 The maximum value a hand can have with all A
# multiply value by sorted index 