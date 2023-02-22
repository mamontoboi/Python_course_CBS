from time import sleep
from abc import ABC, abstractmethod


class Hero(ABC):
    # конструктор класу
    # @abstractmethod
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    # друк параметрів персонажа:
    # @abstractmethod
    def print_info(self):
        print('Рівень здоров\'я:', self.health)
        print('Клас броні:', self.armor, '\n')

    # @abstractmethod
    def damage(value):
        enemy.armor -= value
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

class Warrior(Hero):
    def hello(self):
        print('-> НОВИЙ ГЕРОЙ. Верхом на коні з\'явився бравий воїн на ім\'я', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print('-> УДАР! Хоробрий воїн', self.name, 'атакує', enemy.name, 'мечем!')
        # сила удару для класу Воїн
        Warrior.damage(15)
        print('Страшний удар обрушився на супротивника.\nТепер його броня: ' + str(enemy.armor) +
              ', а рівень здоров\'я: ' + str(enemy.health) + '\n')
        sleep(5)


class Magician(Hero):
    def hello(self):
        print('-> НОВИЙ ГЕРОЙ. Звідки не візьмись з\'явився майстерний чарівник', self.name)
        self.print_info()
        sleep(4)

    def attack(self, enemy):
        print('-> УДАР! Спритний маг', self.name, 'накладає заклинання на', enemy.name)
        # сила удару для класу Маг
        Magician.damage(35)
        print('Складне заклинання приголомшило супротивника.\nТепер його броня: ' + str(enemy.armor) +
              ', а рівень здоров\'я: ' + str(enemy.health) + '\n')
        sleep(5)


Warrior1 = Warrior('Henry', 100, 50)
Warrior1.hello()

Magician1 = Magician('Luke', 50, 20)
Magician1.hello()

Warrior1.attack(Magician1)
Magician1.attack(Warrior1)
