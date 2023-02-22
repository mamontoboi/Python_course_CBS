# Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c.
# Усередині цієї функції створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів)
# та функцію calc_rezult з формальними параметрами зовнішньої функції quadratic_equation. Всередині функції calc_rezult
# здійснити пошук дискримінанта, згідно з результатом якого зробити розрахунок коренів рівняння.
# Зовнішня функція quadratic_equation має повернути перелік значень коренів квадратного рівняння.
# Надати можливість користувачеві ввести з клавіатури формальні параметри для передачі
# їх у створену функцію quadratic_equation, результати роботи функції відобразити на екрані.
import math


def quadratic_equation(a, b, c):
    disc = 0

    def calc_result(a, b, c):
        """
        Calculation of discriminant
        """
        nonlocal disc
        disc = b ** 2 - 4 * a * c
        return disc

    if calc_result(a, b, c) < 0:
        return "No real roots"
    elif calc_result(a, b, c) == 0:
        return -(b / (2 * a))
    else:
        return (- b + math.sqrt(disc)) / (2 * a), (- b - math.sqrt(disc)) / (2 * a)


print(f"The roots of equation:" 
      f"{quadratic_equation((int(input('Enter a = '))), int(input('Enter b = ')), int(input('Enter c = ')))}")
