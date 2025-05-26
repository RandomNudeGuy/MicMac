from pizza_store import PizzaStore

class PizzaDominos(PizzaStore):

    def __init__(self, pizza_id, name, address, employees, phone_number):
        super().__init__(pizza_id, name, address, employees, phone_number)