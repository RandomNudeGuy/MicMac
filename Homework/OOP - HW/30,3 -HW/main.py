from person import Person
from employee import Employee
from animal import Animal
from dog import Dog
from fish import Fish
from bird import Bird


if __name__ == '__main__':
    Man = Employee("james", 12, "microsoft", 1000)

    Man.printt()

    fishie = Fish("nemo", 1, "male", 2 , "shark", 2, "blue")

    fishie.make_sound()