from abc import ABC, abstractmethod

class Pet(ABC):

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def play(self):
        pass