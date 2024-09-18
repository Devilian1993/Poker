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

    def hand_value(self):
        values = self.get_values()
        

    def check_pair(self):
        pass

    def check_straight(self):
        pass

    def check_flush(self):
        pass

