from animal import Animal

class Bird(Animal):

    def __init__(self, name, age, gender, weight, species, wing_span, beak_length):
        super().__init__(name, age, gender, weight)
        self.species = species
        self.wing_span = wing_span
        self.beak_length = beak_length

    def make_sound(self):
        print("Chirp Chird!")

    def move(self):
        print("im flying")