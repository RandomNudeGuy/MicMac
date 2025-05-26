from overrides import overrides
from animal import Animal

class Spider(Animal):
    def __init__(self, name=None):
        super().__init__(8)
        self.name = name

    @overrides
    def eat(self):
        print(f"{self.name} is eating")