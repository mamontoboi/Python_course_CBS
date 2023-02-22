from abc import ABC, abstractmethod
# abc - Abstract Base Classes


class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')


class Dog(Animal):
    def move(self):
        super().move()
        print('Dog moves')


d = Dog()
d.move()
