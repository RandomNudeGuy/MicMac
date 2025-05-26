import datetime

from surprise import Surprise

class Employee:

    def __init__(self, employee_id, first_name, last_name, address, salary, start_date: datetime.datetime, pizza_rank:int, pizza_rank_date: datetime.datetime, surprise: Surprise):
        self