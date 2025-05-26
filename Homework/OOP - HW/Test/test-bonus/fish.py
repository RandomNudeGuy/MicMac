from overrides import overrides
from animal import Animal
from pet import Pet

class Fish(Animal, Pet):
    def __init__(self, name=None):
        super().__init__(0)
        self.name = name

    @overrides
    def getName(self):
        return self.name

    @overrides
    def setName(self, name):
        self.name = name

    @overrides
    def play(self):
        print(f"{self.name} is playing")

    @overrides
    def eat(self):
        print(f"{self.name} is eating")

    @overrides
    def walk(self):
        print(f"{self.name} is swimming")

