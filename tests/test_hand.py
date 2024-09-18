import unittest
from backend.hand import Hand
from backend.card import Card

class TestHand(unittest.TestCase):

    def test_high_card(self):
        cards = [Card("Hearts", 2), Card("Diamonds", 4), Card("Spades", 7), Card("Hearts", "J"), Card("Clubs", 9)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "high card")

    def test_pair(self):
        cards = [Card("Hearts", 2), Card("Diamonds", 5), Card("Clubs", 7), Card("Hearts", "J"), Card("Diamonds", 2)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "pair")

    def test_two_pairs(self):
        cards = [Card("Hearts", 2), Card("Spades", 5), Card("Diamonds", 2), Card("Clubs", 5), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "two pairs")

    def test_three_of_a_kind(self):
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Clubs", 5), Card("Spades", 2), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "three of a kind")

    def test_straight(self):
        cards = [Card("Hearts", 8), Card("Spades", 6), Card("Clubs", 7), Card("Diamonds", 9), Card("Hearts", 5)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "straight")

    def test_flush(self):
        cards = [Card("Hearts", 7), Card("Hearts", 2), Card("Hearts", 4), Card("Hearts", "J"), Card("Hearts", 9)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "flush")

    def test_full_house(self):
        cards = [Card("Hearts", 2), Card("Clubs", 5), Card("Diamonds", 2), Card("Spades", 5), Card("Hearts", 2)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "full house")

    def test_four_of_a_kind(self):
        cards = [Card("Hearts", 2), Card("Clubs", 5), Card("Diamonds", 2), Card("Spades", 2), Card("Hearts", 2)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "four of a kind")

    def test_straight_flush(self):
        cards = [Card("Hearts", 7), Card("Hearts", 9), Card("Hearts", 5), Card("Hearts", 6), Card("Hearts", 8)]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "straight flush")

    def test_royal_flush(self):
        cards = [Card("Hearts", "J"), Card("Hearts", 10), Card("Hearts", "Q"), Card("Hearts", "A"), Card("Hearts", "K")]
        hand = Hand(cards)
        self.assertEqual(hand.hand_value(), "royal flush")

    def test_get_values(self):
        cards = [Card("Hearts", 2), Card("Hearts", 4), Card("Hearts", 7), Card("Hearts", 9), Card("Hearts", "J")]
        hand = Hand(cards)
        self.assertEqual(hand.get_values(), [2, 4, 7, 9, "J"])

    def test_get_suits(self):
        cards = [Card("Hearts", 2), Card("Diamonds", 2), Card("Spades", 2), Card("Clubs", 2), Card("Hearts", 5)]
        hand = Hand(cards)
        self.assertEqual(hand.get_suits(), ["Hearts", "Diamonds", "Spades", "Clubs", "Hearts"])

if __name__ == "__main__":
    unittest.main()