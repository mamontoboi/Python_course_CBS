# Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def __str__(self):
        print(f"Maximum speed of {self.name} is {self.speed} km/h.")


class GroundTransport(Transport):
    def __init__(self, name, speed, terrain_passability):
        super().__init__(name, speed)
        self.terrain_passability = terrain_passability

    def __str__(self):
        super().__str__()
        return f"It has {self.terrain_passability} terrain passability.\n"


class WaterTransport(Transport):
    def __init__(self, name, speed, floatation):
        super().__init__(name, speed)
        self.floatation = floatation

    def __str__(self):
        super().__str__()
        return f"The floatation of the vessel is {self.floatation}.\n"


class AirTransportation(Transport):
    def __init__(self, name, speed, height):
        super().__init__(name, speed)
        self.height = height

    def __str__(self):
        super().__str__()
        return f"The maximum altitude of an aircraft is {self.height} km.\n"


shuttle = AirTransportation('Space Shuttle', 350, 113)
plane = AirTransportation('AirBus A380', 900, 13)
dream = AirTransportation('Ан-225 Мрія', 850, 12)
tanker = WaterTransport('Front Siena', 28, 'positive')
shipwreck = WaterTransport('Moskva', 59, 'negative')
train = GroundTransport('TGV train', 574, 'limited to rails')

print(dream)
print(shuttle)
print(tanker)
print(plane)
print(shipwreck)
print(train)
