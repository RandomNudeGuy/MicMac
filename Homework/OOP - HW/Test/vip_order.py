from overrides import overrides

from order import Order

class VIPOrder(Order):
    def __init__(self, order_id, name, delivery_address, items, customer, payment_type, order_date):
        if customer.customer_type != "VIP":
            raise Exception("Regular customer tried to make a VIP order")
        super().__init__(order_id, name, delivery_address, items, customer, payment_type, order_date)


    @overrides
    def calculate_total_price(self):
        base_price = 0
        for i in self.items:
            base_price += i.price
        if self.customer.customer_discount is None:
            discount = 0
        else:
            discount = self.customer.customer_discount
        discount_price = base_price - discount
        return discount_price
