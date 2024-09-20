from itertools import combinations
from hand import Hand, UTIL_HAND_RANKS


class HandSelector():

    def __init__(self, community_cards, hole_cards):
        self.community_cards = community_cards
        self.hole_cards = hole_cards
        self.combined_cards = community_cards + hole_cards

    def get_all_combinations(self):
        return map(list, combinations(self.combined_cards, 5))

    def select_best_hand(self):
        hand_combinations = list(map(Hand, self.get_all_combinations()))
        hand_combinations.sort()

        return hand_combinations[-1]