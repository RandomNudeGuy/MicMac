class Animal:
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight


    def print_animal(self):
        print(f"name: {self.name}, age: {self.age}, weight: {self.weight}, gender: {self.gender}")

    def make_sound(self):
        print("weeeeeee")

    def move(self):
        print("im moving")