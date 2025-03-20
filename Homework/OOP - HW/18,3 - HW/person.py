
class Person:

    def __init__(self, name, last_name, sex, age, height, animal_ownership):
        self.__name = name
        self.__last_name = last_name
        self.__sex = sex
        self.__age = age
        self.__height = height
        self.__animal_ownership = []

    def print(self):
        print(f'name: {self.__name}. Last Name: {self.__last_name}. Sex: {self.__sex}. Age: {self.__age}. Height: {self.__height}. Animal Ownership: {self.__animal_ownership}')

    def add_animal(self, animal):
        if type(animal) == Animal:
            self.__animal_ownership.append(animal.name)



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def animal_ownership(self):
        return self.__animal_ownership

    @animal_ownership.setter
    def animal_ownership(self, animal_ownership):
        self.__animal_ownership = animal_ownership

class Animal:
    def __init__(self, name, carnivore, sex, age, height):
        self.__name = name
        self.__carnivore  = carnivore
        self.__sex = sex
        self.__age = age
        self.__height = height

    def print(self):
        print(f'name: {self.__name}. Carnivore: {self.__carnivore}. Sex: {self.__sex}. Age: {self.__age}. Height: {self.__height}.')



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def carnivore(self):
        return self.__carnivore

    @carnivore.setter
    def carnivore(self, carnivore):
        self.__carnivore = carnivore

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

class Rectangle:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    def getArea(self):
        return self.__height * self.__width

class Employee:
    def __init__(self, name, year_of_joining, salary, address, monthly_salary, role):
        self.__name = name
        self.__year_of_joining = year_of_joining
        self.__salary = salary
        self.__address = address
        self.__monthly_salary = monthly_salary
        self.__role = role


    def print(self):
        print(f'name: {self.__name}. year of joining: {self.__year_of_joining}. salary: {self.__salary}. address: {self.__address}. mothly salary: {self.__monthly_salary}. role name: {self.__role.name}. role name: {self.__role.description}')

    def __calculate_bonus(self):
        return self.__role.monthly_salary_factor * self.__monthly_salary

    def get_bonus(self):
        print(f"{self.__name} you got {self.__calculate_bonus()} as the annual bonus")

    def promote(self, role):
        self.__role = role

    def getSalary(self):
        return (self.__monthly_salary * 12) + self.__calculate_bonus()

class Role:

    def __init__(self, name, description, monthly_salary_factor):
        self.__name = name
        self.__description = description
        self.__monthly_salary_factor = monthly_salary_factor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def monthly_salary_factor(self):
        return self.__monthly_salary_factor

    @monthly_salary_factor.setter
    def monthly_salary_factor(self, height):
        self.__monthly_salary_factor = monthly_salary_factor

class Company:

    def __init__(self):
        self.employees = []

    def add_employee(self, employe):
        self.employees.append(employe)



    def annual_expense(self):
        employee_total = 0
        for i in self.employees:
            employee_total += i.getSalary()
        return employee_total