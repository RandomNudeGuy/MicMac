from datetime import datetime
from pizza_store import PizzaStore
from employees import Employee
from pizza_hut import PizzaHut

if __name__ == '__main__':
    employee1 = Employee(1, 'Ladis', 'MusWashands', 'Massad', 250, 5 , datetime.strptime('24-10-2002', "%d-%m-%Y"))
    employee2 = Employee(2, 'Emploiz', 'MusWashands', 'Eilabum', 251, 5 , datetime.strptime('23-10-2002', "%d-%m-%Y"))
    employee3 = Employee(3, "Alison", "Bergers", "Eid Al Fiter", 400, 5, datetime.now())

    pizza_hut = PizzaHut(1, 'PizzaHutAshdod', 'Ashdod', [employee1, employee2], '050-7691137')

    print(pizza_hut.calculate_employee_expenses())

    print(pizza_hut.number_of_employees)
    pizza_hut.hire(employee3)
    print(pizza_hut.number_of_employees)

    # pizza_hut.rank_calc()
    print(pizza_hut.store_rank)