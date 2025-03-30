from person import Person


class Employee(Person):
    def __init__(self, name:str, age:int, company:str, salary:int):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def printt(self):
        print(f"name: {self.name} age: {self.age} company: {self.company} salary: {self.salary}")