from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, legs):
        self.legs = legs

    def walk(self):
        print(f"walking on {self.legs} legs")

    @abstractmethod
    def eat(self):
        pass