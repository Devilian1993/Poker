from user import User
from hand import Hand


class Player(User):

    def __init__(self, username, balance, is_bot=False):
        super().__init__(username, balance)
        self.is_bot = is_bot
        self.personal_cards = []
        self.hand = Hand()

