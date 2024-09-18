#High card, pair, two pairs, three of a kind, straight, flush, full house, four of a kind, straight flush, royal flush

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

    def sort_hand(self):
        pass

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
        values = self.get_values()
        suits = self.get_suits()

        if self.check_flush(suits):
            return "flush"

        if self.check_straight(values):
            return "straight"



