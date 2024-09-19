from collections import Counter
from card import UTIL_CARD_VALUES

UTIL_HAND_RANKS = {"high card": 0,
                   "pair": 1,
                   "two pairs": 2,
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

    def get_card_with_count(self, count):
        counter = self.get_counter_dict()

        for card, card_count in counter.items():
            if card_count == count:
                return card

    def get_counter_dict(self):
        return dict(Counter(self.get_values()))

    def count_checker(self, checked_count):
        counter = self.get_counter_dict()

        for count in counter.values():
            if count == checked_count:
                return True

        return False

    # funkcja zwraca wartość karty o danej liczbie wystąpień
    def get_duplicate_hand_strength(self, count):
        counter = self.get_counter_dict()
        return self.get_card_with_count(count)

    # funkcja zwraca najwyższą kartę na ręce LUB 5 TYLKO w przypadku straighta z asem jako pierwsza karta
    def get_highest_card(self):
        if self.get_values() == [2, 3, 4, 5, "A"]:
            return 5
        else:
            return self.get_values()[4]

    def check_straight(self):
        if self.get_values() == [2, 3, 4, 5, "A"]:
            return True
        for i, card in enumerate(self.cards[:3]):
            if card.next_card() != self.cards[i + 1]:
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

    def check_four_of_a_kind(self):
        return self.count_checker(4)

    def check_full_house(self):
        if self.check_three_of_a_kind():
            counter = self.get_counter_dict()

            for count in counter.values():
                if count == 2:
                    return True

        return False

    def check_three_of_a_kind(self):
        return self.count_checker(3)

    def check_two_pairs(self):
        if self.check_pair():
            counter = self.get_counter_dict()

            for card, count in counter.items():
                if count == 2:
                    counter.pop(card)
                    break

            for count in counter.values():
                if count == 2:
                    return True

        return False

    def check_pair(self):
        return self.count_checker(2)

    def hand_value(self):
        self.cards.sort()

        if self.check_royal_flush():
            return "royal flush"

        if self.check_straight_flush():
            return "straight flush"

        if self.check_four_of_a_kind():
            return "four of a kind"

        if self.check_full_house():
            return "full house"

        if self.check_flush():
            return "flush"

        if self.check_straight():
            return "straight"

        if self.check_three_of_a_kind():
            return "three of a kind"

        if self.check_two_pairs():
            return "two pairs"

        if self.check_pair():
            return "pair"

        return "high card"

    # Tej funkcji używamy jak chcemy porównać pozostałe karty (poza szczególnymi układami)
    # Self i other to obiekty (klasy Hand)
    # count_to_delete mówi które karty chcemy usunąć, tzn. karty o jakiej liczebności chcemy usunąć
    # Np. count_to_delete = 3 usuwa karty które występują trzy razy, count_to_delete = 0 nie usuwa żadnej karty
    # comparision mode mówi, czy sprawdzamy czy ręka jest większa ("gt"), mniejsza ("lt") czy równa ("eq")
    # funkcja zwraca True, jeżeli porównanie jest prawdziwe (self.hand > / < / ==) i false w przeciwnym wypadku
    def standalone_card_comparator(self, other, count_to_delete, comparison_mode):
        deleted_card = self.get_card_with_count(count_to_delete)
        self.remaining_cards = [card for card in self.cards if card != deleted_card]
        other.remaining_cards = [card for card in other.cards if card != deleted_card]

        for card1, card2 in zip(self.remaining_cards[::-1], other.remaining_cards[::-1]):
            if comparison_mode == "eq":
                if card1 != card2:
                    return False
            elif comparison_mode == "gt":
                if card1 <= card2:
                    return False
            elif comparison_mode == "lt":
                if card1 >= card2:
                    return False

        return True

    def __lt__(self, other):
        # Podstawowe sprawdzenie, jeżeli są różne układy to od razu zwraca True/False bo nie ma potrzeby dokładnie sprawdzać
        if UTIL_HAND_RANKS[self.hand_value()] != UTIL_HAND_RANKS[other.hand_value()]:
            return UTIL_HAND_RANKS[self.hand_value()] < UTIL_HAND_RANKS[other.hand_value()]
        else:
            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight_flush():
                return UTIL_CARD_VALUES[self.get_highest_card()] < UTIL_CARD_VALUES[other.get_highest_card()]

            # Najpierw sprawdza czy poczwórna karta jest taka sama, jeżeli jest to sprawdza pozostałą
            if self.check_four_of_a_kind():
                if self.get_duplicate_hand_strength(4) != other.get_duplicate_hand_strength(4):
                    return self.get_duplicate_hand_strength(4) < other.get_duplicate_hand_strength(4)
                else:
                    return self.standalone_card_comparator(other, 4, "lt")

            # Najpierw sprawdza potrójną kartę, potem podwójną
            if self.check_full_house():
                if self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3):
                    return self.get_duplicate_hand_strength(3) < other.get_duplicate_hand_strength(3)
                else:
                    return self.get_duplicate_hand_strength(2) < other.get_duplicate_hand_strength(2)

            # Sprawdza po kolei wszystkie karty i porównuje ze sobą
            if self.check_flush():
                return self.standalone_card_comparator(other, 0, "lt")

            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight():
                return UTIL_CARD_VALUES[self.get_highest_card()] < UTIL_CARD_VALUES[other.get_highest_card()]

            # Najpierw sprawdza potrójną kartę, potem pozostałe
            if self.check_three_of_a_kind():
                if self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3):
                    return self.get_duplicate_hand_strength(3) < other.get_duplicate_hand_strength(3)
                else:
                    return self.standalone_card_comparator(other, 3, "lt")

            if self.check_two_pairs():
                # Zapisuje pierwszą parę
                self.first_pair = self.get_duplicate_hand_strength(2)
                other.first_pair = other.get_duplicate_hand_strength(2)

                # Usuwa pierwszą parę z tablicy
                for _ in range(2):
                    self.cards.pop(self.first_pair)
                    other.cards.pop(other.first_pair)

                # Zapisuje drugą parę
                self.second_pair = self.get_duplicate_hand_strength(2)
                other.second_pair = other.get_duplicate_hand_strength(2)

                # Usuwa pierwszą drugą z tablicy
                for _ in range(2):
                    self.cards.pop(self.second_pair)
                    other.cards.pop(other.second_pair)

                # Zapisuje większą parę
                self.bigger_pair = self.first_pair if self.first_pair > self.second_pair else self.second_pair
                other.bigger_pair = other.first_pair if other.first_pair > other.second_pair else other.second_pair

                # Zapisuje mniejszą parę
                self.smaller_pair = self.second_pair if self.first_pair == self.bigger_pair else self.first_pair
                other.smaller_pair = other.second_pair if other.first_pair == other.bigger_pair else other.first_pair

                # Najpierw porównuje większą parę, potem mniejszą, potem pozostałą kartę
                if self.bigger_pair != other.bigger_pair:
                    return self.bigger_pair < other.bigger_pair
                elif self.smaller_pair != other.smaller_pair:
                    return self.smaller_pair != other.smaller_pair
                else:
                    return self.cards[0] < other.cards[0]

            # Najpierw sprawdza podwójną kartę, następnie po kolei pozostałe
            if self.check_pair():
                if self.get_duplicate_hand_strength(2) != other.get_duplicate_hand_strength(2):
                    return self.get_duplicate_hand_strength(2) < other.get_duplicate_hand_strength(2)
                else:
                    return self.standalone_card_comparator(other, 2, "lt")

            # Po kolei porównuje wszystkie karty
            return self.standalone_card_comparator(other, 0, "lt")

    def __eq__(self, other):
        # Jeżeli są różne typy układów to od razu zwraca False, bo wtedy wiadomo że się różnią
        if UTIL_HAND_RANKS[self.hand_value()] != UTIL_HAND_RANKS[other.hand_value()]:
            return False
        else:
            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight_flush():
                return UTIL_CARD_VALUES[self.get_highest_card()] == UTIL_CARD_VALUES[other.get_highest_card()]

            # Najpierw sprawdza czy poczwórna karta jest taka sama, jeżeli nie to zwraca False, jeżeli tak to sprawdza ostatnią kartę
            if self.check_four_of_a_kind():
                if self.get_duplicate_hand_strength(4) != other.get_duplicate_hand_strength(4):
                    return False
                else:
                    return self.standalone_card_comparator(other, 4, "eq")

            # Sprawdza czy potrójna karta jest taka sama i jednocześnie czy podwójna karta jest taka sama
            if self.check_full_house():
                return self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3) \
                       and self.get_duplicate_hand_strength(2) != other.get_duplicate_hand_strength(2)

            # Sprawdza po kolei wszystkie karty i porównuje ze sobą
            if self.check_flush():
                return self.standalone_card_comparator(other, 0, "eq")

            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight():
                return UTIL_CARD_VALUES[self.get_highest_card()] == UTIL_CARD_VALUES[other.get_highest_card()]

            # Najpierw sprawdza czy potrójna karta jest taka sama, jeżeli nie to zwraca False, jeżeli tak to sprawdza pozostałe karty
            if self.check_three_of_a_kind():
                if self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3):
                    return False
                else:
                    return self.standalone_card_comparator(other, 3, "eq")

            if self.check_two_pairs():
                # Zapisuje pierwszą parę
                self.first_pair = self.get_duplicate_hand_strength(2)
                other.first_pair = other.get_duplicate_hand_strength(2)

                # Usuwa pierwszą parę z tablicy
                for _ in range(2):
                    self.cards.pop(self.first_pair)
                    other.cards.pop(other.first_pair)

                # Zapisuje drugą parę
                self.second_pair = self.get_duplicate_hand_strength(2)
                other.second_pair = other.get_duplicate_hand_strength(2)

                # Usuwa drugą parę z tablicy
                for _ in range(2):
                    self.cards.pop(self.second_pair)
                    other.cards.pop(other.second_pair)

                # Zapisuje większą parę
                self.bigger_pair = self.first_pair if self.first_pair > self.second_pair else self.second_pair
                other.bigger_pair = other.first_pair if other.first_pair > other.second_pair else other.second_pair

                # Zapisuje mniejszą parę
                self.smaller_pair = self.second_pair if self.first_pair == self.bigger_pair else self.first_pair
                other.smaller_pair = other.second_pair if other.first_pair == other.bigger_pair else other.first_pair

                # Sprawdza czy większa para jest taka sama i mniejsza para jest taka sama i ostatnia karta jest taka sama
                return self.bigger_pair == other.bigger_pair \
                       and self.smaller_pair == other.smaller_pair \
                       and self.cards[0] == other.cards[0]

            # Sprawdza czy podwójna karta jest taka sama, jeżeli tak to sprawdza pozostałe karty
            if self.check_pair():
                if self.get_duplicate_hand_strength(2) != other.get_duplicate_hand_strength(2):
                    return False
                else:
                    return self.standalone_card_comparator(other, 2, "eq")

            # Po kolei sprawdza wszystkie karty
            return self.standalone_card_comparator(other, 0, "eq")

    def __gt__(self, other):
        # Podstawowe sprawdzenie, jeżeli są różne układy to od razu zwraca True/False bo nie ma potrzeby dokładnie sprawdzać
        if UTIL_HAND_RANKS[self.hand_value()] != UTIL_HAND_RANKS[other.hand_value()]:
            return UTIL_HAND_RANKS[self.hand_value()] > UTIL_HAND_RANKS[other.hand_value()]
        else:
            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight_flush():
                return self.standalone_card_comparator(other, 0, "gt")

            # Najpierw sprawdza czy poczwórna karta jest taka sama, jeżeli jest to sprawdza pozostałą
            if self.check_four_of_a_kind():
                if self.get_duplicate_hand_strength(4) != other.get_duplicate_hand_strength(4):
                    return self.get_duplicate_hand_strength(4) > other.get_duplicate_hand_strength(4)
                else:
                    return self.standalone_card_comparator(other, 4, "gt")

            # Najpierw sprawdza potrójną kartę, potem podwójną
            if self.check_full_house():
                if self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3):
                    return self.get_duplicate_hand_strength(3) > other.get_duplicate_hand_strength(3)
                else:
                    return self.get_duplicate_hand_strength(2) > other.get_duplicate_hand_strength(2)

            # Sprawdza po kolei wszystkie karty i porównuje ze sobą
            if self.check_flush():
                return self.standalone_card_comparator(other, 0, "gt")

            # Wystarczy że sprawdzi najwyższą kartę, bo jak sie zgadza najwyższa karta straighta to reszta też sie zgadza skoro oboje mają straighta
            if self.check_straight():
                return UTIL_CARD_VALUES[self.get_highest_card()] > UTIL_CARD_VALUES[other.get_highest_card()]

            # Najpierw sprawdza potrójną kartę, potem pozostałe
            if self.check_three_of_a_kind():
                if self.get_duplicate_hand_strength(3) != other.get_duplicate_hand_strength(3):
                    return self.get_duplicate_hand_strength(3) > other.get_duplicate_hand_strength(3)
                else:
                    return self.standalone_card_comparator(other, 3, "gt")

            if self.check_two_pairs():
                # Zapisuje pierwszą parę
                self.first_pair = self.get_duplicate_hand_strength(2)
                other.first_pair = other.get_duplicate_hand_strength(2)

                # Usuwa pierwszą parę
                for _ in range(2):
                    self.cards.pop(self.first_pair)
                    other.cards.pop(other.first_pair)

                # Zapisuje drugą parę
                self.second_pair = self.get_duplicate_hand_strength(2)
                other.second_pair = other.get_duplicate_hand_strength(2)

                # Usuwa drugą parę
                for _ in range(2):
                    self.cards.pop(self.second_pair)
                    other.cards.pop(other.second_pair)

                # Zapisuje większą parę
                self.bigger_pair = self.first_pair if self.first_pair > self.second_pair else self.second_pair
                other.bigger_pair = other.first_pair if other.first_pair > other.second_pair else other.second_pair

                # Zapisuje mniejszą parę
                self.smaller_pair = self.second_pair if self.first_pair == self.bigger_pair else self.first_pair
                other.smaller_pair = other.second_pair if other.first_pair == other.bigger_pair else other.first_pair

                # Najpierw porównuje większą parę, potem mniejszą, potem pozostałą kartę
                if self.bigger_pair != other.bigger_pair:
                    return self.bigger_pair > other.bigger_pair
                elif self.smaller_pair != other.smaller_pair:
                    return self.smaller_pair > other.smaller_pair
                else:
                    return self.cards[0] > other.cards[0]

            # Najpierw sprawdza podwójną kartę, następnie po kolei pozostałe
            if self.check_pair():
                if self.get_duplicate_hand_strength(2) != other.get_duplicate_hand_strength(2):
                    return self.get_duplicate_hand_strength(2) > other.get_duplicate_hand_strength(2)
                else:
                    return self.standalone_card_comparator(other, 2, "gt")

            # Po kolei porównuje wszystkie karty
            return self.standalone_card_comparator(other, 0, "gt")

# cards = [Card("Hearts", 2), Card("Spades", 5), Card("Diamonds", 2), Card("Clubs", 5), Card("Hearts", "J")]
# hand = Hand(cards)
# print(hand.cards[0].next_card())
