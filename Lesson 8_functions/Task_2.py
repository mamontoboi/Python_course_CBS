# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів.
# На екрані виведіть таблицю значень цих функцій від -5 до 5 з кроком 0.5.

def squared(a):
    return a ** 2


def cubed(a):
    return a ** 3


i = -5
while -5 <= i <= 5:
    print(f'{i} raised to the power of 2 equals {squared(i)}')
    print(f'{i} raised to the power of 3 equals {cubed(i)}')
    i += 0.5




