

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, delivery_address, customer_type, customer_discount=None):
        self.id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.gift = None


    def remove_fav(self, item_name):
        for i in self.favorite_items:
            if item_name.name == i.name:
                self.favorite_items.remove(i)

    def add_fav(self, item_name):
        if item_name.name not in self.favorite_items:
            self.favorite_items.append(item_name)

    def give_gift(self, gift):
        if self.gift is None:
            self.gift = gift
        else:
            print("Already has a gift!")

    def open_gift(self):
        if self.gift:
            return self.gift.open_gift()
        return "You don't have any gifts!"