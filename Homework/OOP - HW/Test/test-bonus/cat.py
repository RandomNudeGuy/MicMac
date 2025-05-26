from overrides import overrides

from animal import Animal
from pet import Pet


class Cat(Animal, Pet):
    def __init__(self, name=None):
        super().__init__(4)
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