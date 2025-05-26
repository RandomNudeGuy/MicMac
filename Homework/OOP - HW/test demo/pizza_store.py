from abc import ABC, abstractmethod


class PizzaStore(ABC):

    @abstractmethod
    def __init__(self, pizza_id, name, address, employees, phone_number):
        self.pizza_id = pizza_id
        self.name = name
        self.address = address
        self.employees = employees
        self.number_of_employees = self.get_number_of_employees()
        self.phone_number = phone_number

    def get_number_of_employees(self):
        return len(self.employees)

