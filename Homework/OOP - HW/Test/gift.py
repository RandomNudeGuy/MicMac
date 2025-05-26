class Gift:
    def __init__(self, gift_name):
        self.gift_name = gift_name

    def open_gift(self):
        return f"Congratulations! you got a new gift: {self.gift_name}! Enjoy!"
