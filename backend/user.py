class User:

    def __init__(self, username, balance):
        self.username = username
        self.balance = self.get_balance()

    def get_balance(self):
        pass