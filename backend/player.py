from user import User


class Player(User):

    def __init__(self, username, balance, is_bot=False):
        super().__init__(username, balance)
        self.is_bot = is_bot
        self.hand = []

