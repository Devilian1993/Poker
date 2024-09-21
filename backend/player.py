from user import User
from hand import Hand


class Player(User):

    def __init__(self,username, balance, email, password, phone_number, is_bot=False):
        super().__init__(username, balance, email, password, phone_number)
        self.is_bot = is_bot
        self.hole_cards = []
        self.hand = Hand()
        self.current_bet = 0
        self.is_active = True

    def reset_bet(self):
        self.current_bet = 0


    def reset_activity(self):
        self.is_active = True