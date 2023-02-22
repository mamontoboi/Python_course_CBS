# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    speed = 0

    def __speed__(self, value):
        while abs(self.speed) < self.max_speed:
            self.speed += value
            if self.speed > 0:
                print("The car {} is moving with the speed {} km/hr".format(self.name, self.speed))
            elif self.speed == 0:
                print("The car {} is stopped".format(self.name))
            else:
                print("The car {} is moving backwards with the speed {} km/hr".format(self.name, abs(self.speed)))
            return self.speed
        if self.speed > 0 and value < 0:
            self.speed += value
            print("The car {} is moving with the speed {} km/hr".format(self.name, abs(self.speed)))
            return self.speed
        elif self.speed < 0 and value > 0:
            self.speed += value
            print("The car {} is moving backwards with the speed {} km/hr".format(self.name, abs(self.speed)))
        else:
            print("Too fast! Reduce speed!")
        return self.speed

    def change_of_speed(self):
        action = input("W to accelerate \nS to apply the brakes \nF to exit\n").lower()
        if action == "w":
            self.__speed__(10)
            self.change_of_speed()
        elif action == "s":
            self.__speed__(-10)
            self.change_of_speed()
        elif action == "f":
            if self.speed != 0:
                print("You cannot enter while car is moving!\n")
                self.change_of_speed()
            else:
                print("You exited the car")
        else:
            print("Choose what do you want to do? \n")
            self.change_of_speed()


samohod = Car("model T", 70)
samohod.change_of_speed()
