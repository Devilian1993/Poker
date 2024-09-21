
from player import Player
from deck import Deck
import random
from user import User
import time

# Działanie programu.
# -> Program dostaje nastepujace informacje ile botów wczytuje gra (my przyjmujemy, ze 4)
# Nastepnie program wywoluje etapy gry:
# 1) Small Blind (pierwszy gracz od rozdajacego)
# 2) Big Blind (drugi gracz od rozdajacego)
# 3) Nastepuje rozdanie kart
# 4) Pierwsza runda licytacji (AKCJE: CALL, CHECK, RAISE, PASS, ALL IN)
# 5) FLOP
# 6) Druga runda licytacji (AKCJE: ... )
# 7) TURN
# 8) Trzecia runda licytacji (AKCJE : ... )
# 9) RIVER
# 10) Czwarta runda licytacji
# 11) Showdown
# 12) Podział puli


class PokerGame:

    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.community_cards = []
        self.pot = 0  # initial pot
        self.current_bet = 0  # current bet
        self.dealer_index = None  # remember dealer index
        self.game_phase = "pre-flop"

    def table(self):
        print("Players at the table:")
        for player in self.players:
            print(player.username)
        self.dealer_index = random.randint(0, len(self.players) - 1) # losuje dealer'a
        dealer = self.players[self.dealer_index]
        print(f"Starting with player: {dealer.username}")

    def deal_cards(self):   # rozdawanie kart
        random.shuffle(self.deck.deck)
        for player in self.players:
            player.hole_cards = [self.deck.deck.pop(), self.deck.deck.pop()]
        print(f"Your cards: {self.players[0].hole_cards}")


    def smallBlind(self):
        small_blind_index = (self.dealer_index + 1) % len(self.players)  # kolejny gracz od dealer'a jest dealerem  ( % przez liczbe graczy by index nie wyszedl poza liczbe graczy
        small_blind_player = self.players[small_blind_index]

        if small_blind_player.username == "V":   # tutaj zakladamy, ze my sterujemy 'V'. Potem to bedzie trzeba zmienic na logged.username
            while True:
                sb_amount = int(input("How much do you want to bet for Small Blind (1-50): "))
                if sb_amount > 0:
                    break
                else:
                    print("You should enter at least 1.")
        else:
            sb_amount = random.randint(1, 50)   # bot losuje stawke
            print(f"{small_blind_player.username} goes in for Small Blind: {sb_amount}")

        self.pot += sb_amount                   # stawka rosnie o small blind
        self.current_bet = sb_amount            # aktualny bet = small blind
        small_blind_player.balance -= sb_amount # odejmuje balance o kwote zakladu
        print(f"Current pot: {self.pot}")



    def bigBlind(self):   # analogiczne do small blind
        big_blind_index = (self.dealer_index + 2) % len(self.players)  # kolejny gracz po small blindzie
        big_blind_player = self.players[big_blind_index]


        if big_blind_player.username == "V":  # my sterujemy tylko 'V'
            while True:
                bb_amount = int(input(f"How much do you want to bet for Big Blind (more than {self.current_bet}): "))
                if bb_amount > self.current_bet:  # sprawdza czy wchodizmy za wiecej niz jest bet
                    break
                else:
                    print("Your bet cannot be lower than current bet")

        else:
            bb_amount = random.randint(51, 75)
            print(f"{big_blind_player.username} goes in for Big Blind: {bb_amount}")

        self.pot += bb_amount
        self.current_bet = bb_amount
        big_blind_player.balance -= bb_amount
        print(f"Current pot: {self.pot}")

    def flop(self):
        self.game_phase = "flop"
        print("\n==== FLOP ====")
        for _ in range(3):
            card = self.deck.deck.pop()
            self.community_cards.append(card)
        print(f"Community cards: {self.community_cards}")

    def turn(self):
        self.game_phase = "turn"
        print("\n==== TURN ====")
        card = self.deck.deck.pop()
        self.community_cards.append(card)
        print(f"Community cards: {self.community_cards}")

    def river(self):
        self.game_phase = "river"
        print("\n==== RIVER ====")
        card = self.deck.deck.pop()
        self.community_cards.append(card)
        print(f"Community cards: {self.community_cards}")

    def negotiation(self):
        pass

    def play_round(self, starting_index):
        for i in range(len(self.players)):
            current_player = self.players[(starting_index + i) % len(self.players)]   # wyznaczamy aktualnego gracza
            self.negotiation(current_player)

    def game(self):
        self.table()
        time.sleep(2)

        # Small Blind and Big Blind
        self.smallBlind()
        time.sleep(2)
        self.bigBlind()
        time.sleep(2)

        # Deal cards
        self.deal_cards()
        time.sleep(2)

        # Pierwsza faza negocjacji
        starting_index = (self.dealer_index + 3) % len(self.players)
        self.play_round(starting_index)
        time.sleep(2)

        # Flop
        self.flop()
        time.sleep(2)

        # Druga faza negocjacji.
        starting_index = (self.dealer_index + 1) % len(self.players)
        self.play_round(starting_index)
        time.sleep(2)

        # Turn
        self.turn()
        time.sleep(2)

        # Trzecia faza negocjacji
        self.play_round(starting_index)
        time.sleep(2)

        # River
        self.river()
        time.sleep(2)

        # Czwarta faza negocjacji
        self.play_round(starting_index)
        time.sleep(2)

        # Showdown
        print("\n === Showdown ===")
        print(f"Community cards: {self.community_cards}")
        # potem tu winnera wyznaczy
        time.sleep(2)



game = PokerGame([
    Player("V", 1000, "v@v.com", 123456, 739),
    Player("VernonRoche", 1000, "wolna@temeria.tm", 1209321, 3201),
    Player("Takemura", 1000, "jebac@arasake.com", 129321, 2500),
    Player("Geralt", 1000, "kaedwen@kaermorhen.blaviken", 892101, 3021)
])

game.game()
