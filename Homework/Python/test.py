class Employee:
    def __init__(self, name, work_hours):
        self.name = name
        self.work_hours = work_hours

class Company:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_work_hours(self):
        total = 0
        for employee in self.employees:
            total += employee.work_hours
        return total

    def print_company_info(self):
        print("Company has employees: ")
        for employer in self.employees:
            print(f"Name: {employer.name}, Work hours: {employer.work_hours}")
        print(f"Total work hours in company are: {self.total_work_hours()}")


if __name__ == "__main__":
    alice = Employee('Alice', 40)
    bob = Employee('Bob', 50)
    charlie = Employee('Charlie', 60)
    company1 = Company()
    company1.add_employee(alice)
    company1.add_employee(bob)
    company2 = company1
    company1.add_employee(charlie)
    print("Company 1 Information: ")
    company1.print_company_info()
    print("Company 2 Information: ")
    company2.print_company_info()