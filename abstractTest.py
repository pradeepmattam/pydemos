from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def implement_me(self):
        pass


class Honda(Vehicle):

    def implement_me(self):
        print('Great Build')


honda = Honda()

