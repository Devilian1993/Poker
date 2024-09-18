class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def next_card(self):
        if isinstance(self.value, int):
            if self.value == 10:
                return "J"
            else:
                return self.value + 1
        else:
            if self.value == "J":
                return "Q"
            elif self.value == "Q":
                return "K"
            elif self.value == "K":
                return "A"
            else:
                return None