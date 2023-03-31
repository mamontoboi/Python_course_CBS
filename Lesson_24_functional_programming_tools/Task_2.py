# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.

from random import randint


def gen(rng):
    for _ in range(rng):
        yield randint(1, 10)


lst = list(gen(30))
print(lst)


print(list(map(lambda x: x ** 2, (filter(lambda x: x % 2 == 1, lst)))))



