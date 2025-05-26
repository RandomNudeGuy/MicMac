from overrides import override
from pizza_store import PizzaStore
from employees import Employee

class PizzaHut(PizzaStore):
    def __init__(self, pizza_id, name, address, list_of_employees, phone_number):
        super().__init__(pizza_id, name, address, list_of_employees, phone_number)

    @override
    def rank_calc(self):
        store_rank = 0
        for i in self.list_of_employees:
            store_rank += i.pizza_rank
        self.store_rank = store_rank / self.number_of_employees



