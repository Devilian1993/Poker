
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

    import time

    def negotiation(self, player):
        if not player.is_active:  # jezeli gracz not is_active, to go pomijamy przy negocjacjach
            return

        if player.username == "V":  # Sterowanie tylko 'V' (potem trzeba to zamienic na logged_user.username na dalszym etapie
            while True:
                print(f"Current pot: {self.pot}, Your balance: {player.balance}")
                print(f"Choose your action. Available action's: ")


                # ----------------------------
                # == SPRAWDZA DOSTEPNE AKCJE =
                # ----------------------------
                available_actions = []


                if player.current_bet == self.current_bet:
                    available_actions.append("check")  # gdy current_bet = self.current_bet

                available_actions.append("pass")  # zawsze mozna pass

                if player.balance >= (self.current_bet - player.current_bet):  # gdy moze call
                    available_actions.append("call")

                if player.balance > self.current_bet:  # gdy moze raise
                    available_actions.append("raise")

                #print(available_actions)
                # wyswietla dostepne akcje



                if "call" in available_actions and "raise" in available_actions and "check" in available_actions:
                    print("Call, Raise, Check and Pass")

                elif "check" in available_actions:
                    print("Check and Pass")

                elif "call" in available_actions and "check" in available_actions:
                    print("Call, Check and Pass")

                elif "pass" in available_actions and "call" in available_actions and "raise" in available_actions:
                    print("Call, Raise and Pass.")

                elif "pass" in available_actions:
                    print("Pass")


                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

                action = input("Choose an action : ").lower()

                if action == "pass":
                    print(f"{player.username} passes.")
                    time.sleep(1.5)
                    player.is_active = False   # wyłącza nas z gry
                    return

                elif action == "check" and "check" in available_actions:   # warunek na check
                    print(f"{player.username} checks.")
                    time.sleep(1.5)
                    return

                elif action == "call" and "call" in available_actions:
                    call_amount = self.current_bet - player.current_bet
                    player.balance -= call_amount
                    player.current_bet += call_amount
                    self.pot += call_amount
                    print(f"{player.username} calls, adding {call_amount} to the pot.")
                    time.sleep(1.5)
                    return

                elif action == "raise" and "raise" in available_actions:
                    while True:
                        raise_amount = input(f"How much do you want to raise? (minimum: {self.current_bet + 1}): ")
                        if raise_amount.isnumeric():
                            raise_amount = int(raise_amount)
                            player.balance -= raise_amount
                            player.current_bet += raise_amount
                            self.pot += raise_amount
                            self.current_bet = raise_amount
                            print(f"{player.username} raises to {raise_amount}.")
                            time.sleep(1.5)
                            break

                        else:
                            print(f"Invalid raise amount.")

                else:
                    print("This option is not available.")
                    time.sleep(1.5)



        ## tu logika dla bota

        else:  # Bot logic
            print(f"{player.username}'s turn (bot).")
            time.sleep(1.5)

            # ----------------------------
            # == SPRAWDZA DOSTEPNE AKCJE =
            # ----------------------------



            available_actions = []


            if player.current_bet == self.current_bet:
                available_actions.append("check")  # gdy current_bet = self.current_bet

            available_actions.append("pass")  # zawsze mozna pass

            if player.balance >= (self.current_bet - player.current_bet):  # gdy moze call
                available_actions.append("call")

            if player.balance > self.current_bet:  # gdy moze raise
                available_actions.append("raise")

            # na potrzebe symulacji ustalilem losowo akcje bota
            # nie podpinalem tego do niczego bo jest to mocno "hardkorowa" wersja + nie potrafie tego zrobic na szybko

            if "check" not in available_actions and "raise" in available_actions and "call" in available_actions:  # gdy nie mozemy check
                action_probabilities = {"pass": 0.3, "call": 0.4, "raise": 0.3}

            if "check" in available_actions and "call" not in available_actions and "raise" not in available_actions:
                action_probabilities = {"check": 1.0, "pass": 0.0, "call": 0.0, "raise": 0.0}

            if player.balance < self.current_bet and "check" not in available_actions:  # gdy mozemy tylko pass
                action_probabilities = {"pass": 1.0}




    # w play_round trzeba zmienic jedna rzecz
    # negocjacje nie dzialaja w prawidlowy sposob
    # tzn.
    # np jak gra czterech graczy
    # A : check
    # B : check
    # C : raise
    # D : call
    # tu konczy sie kolejka, a powinno pojsc jeszcze 'jedna' tura az do tego co 'raise'
    # czyli potem D, A, B, C
    # DOPOKI AZ KAZDY GRACZ NIE ZAGRA check albo pass
    # Jezeli chodzi o ALL-IN to tego w ogole nie robilem na razie
    # Na razie boty (stan na 21.09.2024 na 16:05) nie podejmują w ogóle decyzji


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
        print("The winner is : {winner_username}")



game = PokerGame([
    Player("V", 1000, "v@v.com", 123456, 739),
    Player("VernonRoche", 1000, "wolna@temeria.tm", 1209321, 3201),
    Player("Takemura", 1000, "jebac@arasake.com", 129321, 2500),
    Player("Geralt", 1000, "kaedwen@kaermorhen.blaviken", 892101, 3021)
])

game.game()
