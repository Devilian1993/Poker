import unittest
from backend.hand import Hand
from backend.card import Card

class TestHand(unittest.TestCase):

    def test_high_card(self):
        # High card example: 2 of Hearts, 4 of Diamonds, 7 of Spades, 9 of Clubs, Jack of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 4), Card("Spades", 7), Card("Clubs", 9), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "high card")

    def test_pair(self):
        # Pair example: 2 of Hearts, 2 of Diamonds, 5 of Spades, 7 of Clubs, Jack of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 5), Card("Clubs", 7), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "pair")

    def test_two_pairs(self):
        # Two pairs example: 2 of Hearts, 2 of Diamonds, 5 of Spades, 5 of Clubs, Jack of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 5), Card("Clubs", 5), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "two pairs")

    def test_three_of_a_kind(self):
        # Three of a kind example: 2 of Hearts, 2 of Diamonds, 2 of Spades, 5 of Clubs, Jack of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 2), Card("Clubs", 5), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "three of a kind")

    def test_straight(self):
        # Straight example: 5 of Hearts, 6 of Diamonds, 7 of Spades, 8 of Clubs, 9 of Hearts
        cards = [Card("Hearts", 5), Card("Diamonds", 6), Card("Spades", 7), Card("Clubs", 8), Card("Hearts", 9)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "straight")

    def test_flush(self):
        # Flush example: 2 of Hearts, 4 of Hearts, 7 of Hearts, 9 of Hearts, Jack of Hearts
        cards = [Card("Hearts", 2), Card("Hearts", 4), Card("Hearts", 7), Card("Hearts", 9), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "flush")

    def test_full_house(self):
        # Full house example: 2 of Hearts, 2 of Diamonds, 2 of Spades, 5 of Clubs, 5 of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 2), Card("Clubs", 5), Card("Hearts", 5)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "full house")

    def test_four_of_a_kind(self):
        # Four of a kind example: 2 of Hearts, 2 of Diamonds, 2 of Spades, 2 of Clubs, 5 of Hearts
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 2), Card("Clubs", 2), Card("Hearts", 5)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "four of a kind")

    def test_straight_flush(self):
        # Straight flush example: 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts
        cards = [Card("Hearts", 5), Card("Hearts", 6), Card("Hearts", 7), Card("Hearts", 8), Card("Hearts", 9)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "straight flush")

    def test_royal_flush(self):
        # Royal flush example: 10 of Hearts, Jack of Hearts, Queen of Hearts, King of Hearts, Ace of Hearts
        cards = [Card("Hearts", 10), Card("Hearts", "J"), Card("Hearts", "Q"), Card("Hearts", "K"), Card("Hearts", "A")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "royal flush")

    def test_get_values(self):
        cards = [Card("Hearts", 2), Card("Hearts", 4), Card("Hearts", 7), Card("Hearts", 9), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.get_values(), [2, 4, 7, 9, "J"])

    def test_get_suites(self):
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 2), Card("Clubs", 2), Card("Hearts", 5)]
        hand = Hand(cards)
        self.assertEqual(hand.get_suites(), ["Hearts", "Diamonds", "Spades", "Clubs", "Hearts"])

if __name__ == "__main__":
    unittest.main()