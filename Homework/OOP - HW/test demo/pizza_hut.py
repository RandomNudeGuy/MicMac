from pizza_store import PizzaStore

class PizzaHut(PizzaStore):

    def __init__(self, pizza_id, name, address, employees, phone_number):
        super().__init__(pizza_id,name,  address,employees, phone_number )