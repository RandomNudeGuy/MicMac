
class Car:

    def __init__(self, brand, subbrand, speed, fuel, color):
        self.__brand = brand
        self.__subbrand = subbrand
        self.__speed = speed
        self.__fuel = fuel
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


    @property
    def subbrand(self):
        return self.__subbrand

    @subbrand.setter
    def subbrand(self, subbrand):
        self.__subbrand = subbrand

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


