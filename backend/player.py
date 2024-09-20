from user import User
from hand import Hand


class Player(User):

    def __init__(self,username, balance, email, password, phone_number, is_bot=False):
        super().__init__(username, balance, email, password, phone_number)
        self.is_bot = is_bot
        self.hole_cards = []
        self.hand = Hand()

