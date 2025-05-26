import datetime
from abc import ABC, abstractmethod
from datetime import timedelta

from employees import Employee


class PizzaStore(ABC):
    def __init__(self, pizza_id, name, address, list_of_employees, phone_number):
        self.pizza_id = pizza_id
        self.name = name
        self.address = address
        self.number_of_employees = len(list_of_employees)
        self.list_of_employees = list_of_employees
        self.phone_number = phone_number
        self.store_rank = None
        self.rank_calc()

    def calculate_employee_expenses(self):
        total_salary = 0
        for i in self.list_of_employees:
            total_salary += i.salary # :)
        return total_salary

    def hire(self, employee):
        if employee in self.list_of_employees:
            return "Employee Already Hired!"
        else:
            self.list_of_employees.append(employee)
            self.number_of_employees = len(self.list_of_employees)


    def fire(self, employee):
        if employee in self.list_of_employees:
            self.list_of_employees.remove(employee)
            self.number_of_employees = len(self.list_of_employees)

    @abstractmethod
    def rank_calc(self):
        pass


    def calculate_range_rank(self, rank_range:int) -> int:
        if self.number_of_employees > 0:
            current_date = datetime.datetime.now()
            validate_date = current_date - datetime.timedelta(rank_range)

            for employee in self.list_of_employees
                if validate_date > employee.pizza_rank_date:
                    
        else:
            return 0