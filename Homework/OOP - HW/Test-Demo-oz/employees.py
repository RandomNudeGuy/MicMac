from datetime import datetime


class Employee():
    def __init__(self, employee_id, first_name, last_name, address, salary, pizza_rank:int, pizza_rank_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.salary = salary
        self.start_date = datetime.now()
        self.pizza_rank = pizza_rank
        self.pizza_rank_date = pizza_rank_date
        self.surprise = None


    @property
    def get_salary(self):
        return self.salary

