import unittest
from backend.hand import Hand
from backend.card import Card
from backend.deck import Deck

class TestHand(unittest.TestCase):
    def setUp(self):
        # ROYAL FLUSH -> STR8 FLUSH -> FOUR OF A KIND -> FULL_HOUSE -> STR8 -> THREE OF A KIND -> TWO PAIRS -> PAIR -> HIGH CARD
        self.royal_flush = Hand([
            Card("Hearts", 10),
            Card("Hearts", "J"),
            Card("Hearts", "Q"),
            Card("Hearts", "K"),
            Card("Hearts", "A"),
        ])

        self.straight_flush = Hand([
            Card("Hearts", 3),
            Card("Hearts", 4),
            Card("Hearts", 5),
            Card("Hearts", 6),
            Card("Hearts", 7),
        ])

        self.four_of_a_kind = Hand([
            Card("Hearts", 10),
            Card("Spades", 10),
            Card("Clubs", 10),
            Card("Diamonds", 10),
            Card("Hearts", "A"),
        ])

        self.full_house = Hand([
            Card("Hearts", 10),
            Card("Clubs", 10),
            Card("Hearts", "Q"),
            Card("Diamonds", "Q"),
            Card("Spades", "Q"),
        ])

        self.straight = Hand([
            Card("Clubs", 2),
            Card("Hearts", 3),
            Card("Spades", 4),
            Card("Diamonds", 5),
            Card("Clubs", 6),
        ])

        self.three_of_a_kind = Hand([
            Card("Hearts", 10),
            Card("Spades", 10),
            Card("Diamonds", 10),
            Card("Hearts", "K"),
            Card("Hearts", "A"),
        ])

        self.two_pairs = Hand([
            Card("Hearts", 10),
            Card("Spades", 10),
            Card("Hearts", "Q"),
            Card("Spades", "Q"),
            Card("Diamonds", "Q"),
        ])

        self.pair = Hand([
            Card("Hearts", 10),
            Card("Spades", 10),
            Card("Hearts", 8),
            Card("Spades", 5),
            Card("Diamonds", 3),
        ])

        self.high_card = Hand([
            Card("Hearts", 10),
            Card("Spades", 3),
            Card("Hearts", 4),
            Card("Spades", 8),
            Card("Diamonds", 9),
        ])

    #22.30 -> 23.28

    def test_royal_flush_vs_straight_flush(self):
        self.assertTrue(self.royal_flush > self.straight_flush)
    def test_straight_flush_vs_four_of_a_kind(self):
        self.assertTrue(self.straight_flush > self.four_of_a_kind)
    def test_four_of_a_kind_vs_full_house(self):
        self.assertTrue(self.four_of_a_kind > self.full_house)
    def test_full_house_vs_straight(self):
        self.assertTrue(self.full_house > self.straight)
    def test_straight_vs_three_of_a_kind(self):
        self.assertTrue(self.straight > self.three_of_a_kind)
    def test_three_of_a_kind_vs_two_pairs(self):
        self.assertTrue(self.three_of_a_kind > self.two_pairs)
    def test_two_pairs_vs_pair(self):
        self.assertTrue(self.two_pairs > self.pair)
    def test_pair_vs_high_card(self):
        self.assertTrue(self.pair > self.high_card)

# RANDOMOWE DWIE TALIE
        #


if __name__ == '__main__':
    unittest.main()
