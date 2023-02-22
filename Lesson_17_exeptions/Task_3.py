# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури.
# Виведіть усіх співробітників, які були прийняті після цього року.

class NotLetters(Exception):
    def __str__(self):
        return f'Must contain only letters!'


class Employee:
    def __init__(self, first, last, dept, year):
        self.first = first
        self.last = last
        self.dept = dept
        self.year = year

    def __str__(self):
        return '{} {} is a member of {} since {}'.format(self.first, self.last, self.dept, self.year)

    @staticmethod
    def check_letters(value):
        if value.isalpha():
            return value
        else:
            raise NotLetters

    @staticmethod
    def new_employee():
        while True:
            first = input(f"Please write the first name of the Employee: ").title()
            try:
                first = Employee.check_letters(first)
                break
            except NotLetters:
                print('Must contain only letters!')
                continue
        while True:
            last = input(f"Please write the last name of the Employee: ").title()
            try:
                last = Employee.check_letters(last)
                break
            except NotLetters:
                print('Must contain only letters!')
                continue
        while True:
            dept = input(f"Please write the department the Employee is currently working in: ").title()
            try:
                dept = Employee.check_letters(dept)
                break
            except NotLetters:
                print('Must contain only letters!')
                continue
        while True:
            year = input('Please write when the Employee started to work in the Department: ')
            try:
                year = int(year)
                break
            except ValueError:
                print('Must contain only numbers!')
                continue
        return Employee(first, last, dept, year)

the_one = Employee('Paul', 'Anderson', 'some corp', 1999)
print(the_one)

smith = Employee.new_employee()
print(smith)
