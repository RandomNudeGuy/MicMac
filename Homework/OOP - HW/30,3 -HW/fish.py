from animal import Animal

class Fish(Animal):

    def __init__(self, name, age, gender, weight, species, fin_count, scale_color):
        super().__init__(name, age, gender, weight)
        self.species = species
        self.fin_count = fin_count
        self.scale_color = scale_color

    def make_sound(self):
        super().make_sound()
        print("fish not making a sound")

    def move(self):
        print("im swimming")