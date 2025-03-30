from animal import Animal

class Dog(Animal):

    def __init__(self, name, age, gender, weight, breed, tail_length:int, bark_volume:int):
        super().__init__(name, age, gender, weight)
        self.breed = breed
        self.tail_length = tail_length
        self.bark_volume = bark_volume

    def make_sound(self):
        print(f"{self.bark_volume} Woof!")

    def move(self):
        print("im running")