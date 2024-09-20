from player import Player
from deck import Deck
import random

class PokerGame:

    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.community_cards = []
        self.deal_cards()

    def deal_cards(self):
        random.shuffle(self.deck.deck)

        for player in self.players:
            player.hole_cards = [self.deck.deck.pop(), self.deck.deck.pop()]

    def flop(self):
        for i in range(3):
            self.community_cards.append(self.deck.deck.pop())

    def turn(self):
        self.community_cards.append(self.deck.deck.pop())

    def river(self):
        self.community_cards.append(self.deck.deck.pop())

#game = PokerGame([Player("V", 1000), Player("Geralt", 1000)])

