from person import Person
from person import Animal
from person import Rectangle
from person import Employee
from person import Role
from person import Company

if __name__ == '__main__':
    student1 = Person('Jonathan', 'Tzur', 'Male', 22, 171, None)
    student2 = Person('Rawi', 'Brown', 'Male', 20, 168, None)
    student3 = Person('Hadas', 'Hason', 'Female', 20, 169, None)

    #Print the class type of each instance.
    print(f'{student1.name} is class type: {type(student1)}')
    print(f'{student2.name} is class type: {type(student2)}')
    print(f'{student3.name} is class type: {type(student3)}')

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

    #For your first student instance - Use getattr() and setatter() Python functions to change attribute values and get attribute values.
    print(student1.name)
    student1.name = 'JoJo'
    print(student1.name)

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

    #For your second student instance - Use simple attribute access (using . to change attribute value and get attribute value).
    print(student2.age)
    student2.age = 21
    print(student2.age)

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

    print(student1.animal_ownership)
    student1.animal_ownership.append('Hell')
    print(student1.animal_ownership)
    student1.animal_ownership.remove('Hell')
    print(student1.animal_ownership)

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    animal1 = Animal('Dolphin', True, 'Male', 10, 171)
    student1.add_animal(animal1)
    print(student1.animal_ownership)

    rectange1 = Rectangle(5, 4)
    print(rectange1.getArea())

    employee1 = Employee('Robert', 1994, 12000, '64C- WallsStreat',1000, Role("Managaer", "CEO", 2))
    employee2 = Employee('Sam', 2000, 11000, '68D- WallsStreat', 1000, Role("Managaer", "CEO", 2))
    # employee3 = Employee('John', 1999, 11000, '26B- WallsStreat', 1000)

    # employee1.print()
    # employee2.print()
    # employee3.print()

    company1 = Company()
    company1.add_employee(employee1)
    company1.add_employee(employee2)

    employee1.get_bonus()
    print(company1.annual_expense())

