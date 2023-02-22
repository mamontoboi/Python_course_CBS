# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості.
# Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати
# температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class TempConverter:
    def __init__(self):
        self._temp = None
        self._scale = None

    @property
    def value(self):  # works as getter
        print(f'{self._value} {self._scale}')

    @value.setter
    def value(self, figure):
        value, scale = figure.split(' ')
        self._value = int(value)
        self._scale = scale

    @value.deleter
    def value(self):
        del self._temp, self._scale

    def convert(self):
        if self._scale == 'F':
            self._value = (self._value - 32) / 1.8
            self._scale = 'C'
        else:
            self._value = self._value * 1.8 + 32
            self._scale = 'F'
        return f"{round(self._value, 2)} {self._scale}"



temp = TempConverter()
temp.value = '35 C'  # setter in operation
temp.value  # getter in operation
print(temp.convert())  # converts to 95 F
temp.value
print(temp.convert())  # convers back to 35 C
temp.value
del temp
# temp.value  # gives Traceback after deletion

temp2 = TempConverter()
temp2.value = '90 F'  # activation of setter, gives values to the instance
temp2.value  # rcvs data of the instance
print(temp2.convert())  # converts the data and returns it
