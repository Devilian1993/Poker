from itertools import combinations
from hand import Hand


class HandSelector():

    def __init__(self, community_cards, hole_cards):
        self.community_cards = community_cards
        self.hole_cards = hole_cards
        self.combined_cards = community_cards + hole_cards
        self.select_best_hand()

    def get_all_combinations(self):
        return combinations(self.combined_cards, 5)

    def select_best_hand(self):
        pass