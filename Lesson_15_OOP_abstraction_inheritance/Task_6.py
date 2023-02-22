from datetime import date


class MyClass1:
    def __init__(self, surname, name, age, country):
        self.surname = surname
        self.name = name
        self.age = age
        self.country = country
        self.is_adult(surname, name, age, country)

    number_of_adults_Ukraine = 0
    number_of_adults_Puerto_Rico = 0

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear, country):
        return cls(surname, name, date.today().year - birthYear, country)

    @classmethod
    def is_adult(cls, surname, name, age, country):
        if country == 'Ukraine' and age >= 18:
            print(f"{name} {surname} is adult in {country}")
            MyClass1.number_of_adults_Ukraine += 1
        elif country == 'Puerto Rico' and age >= 21:
            MyClass1.number_of_adults_Puerto_Rico += 1
            print(f"{name} {surname} is adult in {country}")
        else:
            print(f"{name} {surname} is underage both in Ukraine and in Puerto Rico.")

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19, 'Ukraine')

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000, 'Ukraine')

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010, 'Puerto Rico')

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001, 'Puerto Rico')

print(f'Number of adults in Ukraine is {MyClass1.number_of_adults_Ukraine}')
print(f'Number of adults in Puerto Rico is {MyClass1.number_of_adults_Puerto_Rico}')
