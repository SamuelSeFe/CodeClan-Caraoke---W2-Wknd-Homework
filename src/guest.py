class Guest:
    def __init__(self, _name, _wallet, _fav_song):
        self.name = _name
        self.wallet = _wallet
        self.fav_song = _fav_song

    def check_wallet(self, cash):
        return self.wallet >= cash

    def remove_money_from_wallet(self, cash):
        self.wallet -= cash