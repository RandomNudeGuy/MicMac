from person import Person
from person import Animal
from person import Rectangle
import pandas as pd

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


