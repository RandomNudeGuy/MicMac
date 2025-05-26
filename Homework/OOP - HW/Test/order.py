from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, order_id, name, delivery_address, items, customer, payment_type, order_date):
        self.id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = order_date
        self.total_price = self.calculate_total_price()
        self.update_customer_favorites()

    @abstractmethod
    def calculate_total_price(self):
        pass

    def update_customer_favorites(self):
        for item in self.items:
            if item.name not in self.customer.favorite_items: # checking if item is already there by item name
                self.customer.favorite_items.append(item) #adding item to fav
