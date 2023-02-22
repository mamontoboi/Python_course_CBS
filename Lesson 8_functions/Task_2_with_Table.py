# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів.
# На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.

from prettytable import PrettyTable


def squared(a):
    """
    This function squares the given values
    Returns: actual value squared

    """
    return a ** 2


def mults(a):
    """
    This function multiplies the given values by 2
    Returns: Product of multiplication

    """
    return a * 2


table = PrettyTable()
table.field_names = ['Initial value', 'Product of multiplication *2', 'Value squared']

i = -5
while -5 <= i <= 5:
    func_mult = mults(i)
    func_squared = squared(i)
    table.add_row([i, func_mult, func_squared])
    i += 0.5

print(table)
