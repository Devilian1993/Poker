#High card, pair, two pairs, three of a kind, straight, flush, full house, four of a kind, straight flush, royal flush
#from card import Card
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

    def check_straight(self):
        if self.get_values() == [2, 3, 4, 5, "A"]:
            return True
        for i, card in enumerate(self.cards[:3]):
            if card.next_card() != self.cards[i+1]:
                return False
        return True

    def check_flush(self):
        suits = self.get_suits()
        if len(list(set(suits))) == 1:
            return True
        else:
            return False

    def check_straight_flush(self):
        return self.check_flush() and self.check_straight()

    def check_royal_flush(self):
        return self.check_flush() and self.get_values() == [10, "J", "Q", "K", "A"]


    def hand_value(self):
        self.cards.sort()
        values = self.get_values()

        if self.check_royal_flush():
            return "royal flush"

        if self.check_straight_flush():
            return "straight flush"

        if self.check_flush():
            return "flush"

        if self.check_straight():
            return "straight"

    def __lt__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] < UTIL_HAND_RANKS[other.hand_value()]

    def __eq__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] == UTIL_HAND_RANKS[other.hand_value()]

    def __gt__(self, other):
        return UTIL_HAND_RANKS[self.hand_value()] > UTIL_HAND_RANKS[other.hand_value()]

#cards = [Card("Hearts", 2), Card("Spades", 5), Card("Diamonds", 2), Card("Clubs", 5), Card("Hearts", "J")]
#hand = Hand(cards)
#print(hand.cards[0].next_card())
