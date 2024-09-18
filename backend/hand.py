#High card, pair, two pairs, three of a kind, straight, flush, full house, four of a kind, straight flush, royal flush
from card import Card
UTIL_HAND_RANKS = {"high card": 0,
            "pair": 1,
            "two pair": 2,
            "three of a kind": 3,
            "straight": 4,
            "flush": 5,
            "full house": 6,
            "four of a kind": 7,
            "straight flush": 8,
            "royal flush": 9
        }

class Hand:

    def __init__(self, cards=None):
        if cards is None:
            cards = []
        else:
            self.cards = cards

    def get_values(self):
        values = []
        for card in self.cards:
            values.append(card.value)

        return values

    def get_suits(self):
        suits = []
        for card in self.cards:
            suits.append(card.suit)

        return suits

    def check_pair(self):
        pass

    @staticmethod
    def check_straight(values):
        pass

    @staticmethod
    def check_flush(suits):
        if len(list(set(suits))) == 1:
            return True
        else:
            return False

    def hand_value(self):
        self.cards.sort()
        values = self.get_values()
        suits = self.get_suits()


        if self.check_flush(suits):
            return "flush"

        if self.check_straight(values):
            return "straight"

    def __lt__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] < UTIL_HAND_RANKS[other.hand_value()]

    def __eq__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] == UTIL_HAND_RANKS[other.hand_value()]

    def __gt__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] > UTIL_HAND_RANKS[other.hand_value()]


