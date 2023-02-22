# example_4.py
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __test(self, b=None):  # private method. Works "only" within the class
        self.a = 5
        self.b = b
        print(self.a, self.b)

    def setTest(self, c):  # setter. Sends value to the private method
        self.__test(c)

    def getTest(self):  # getter. Rcvs response from private method.
        return self.__test()


t = Test(1, 2)
# t._Test__test() # Not recommended way of addressing the private method
t.getTest()  # 5 None -- because those parameters were preassigned and not changed by getter
t.setTest(10)  # 5 10, because 10 were passed as b instead of None.
t.getTest()  # 5 None


class Car:
    def __init__(self, name, mileage):
        self.name = name
        self._mileage = mileage

    def __str__(self):
        return f'{self.name} {self._mileage}'

    def set_mileage(self, value):
        self._mileage = value

    def get_milage(self):
        return self._mileage


car1 = Car('jaguar', 20000)
print(car1)

car1.set_mileage(30000)
print(car1)

print(car1.get_milage())