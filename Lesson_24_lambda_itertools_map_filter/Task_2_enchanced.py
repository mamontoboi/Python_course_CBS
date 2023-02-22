# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.

from random import randint


def gen(rng):
    for _ in range(rng):
        yield randint(1, 10)


# same as
def new_gen(rng):
    yield from [randint(1, 10) for _ in range(rng)]


lst = list(gen(30))
print(lst)

new_lst = list(new_gen(30))
print(new_lst)

print(list(map(lambda x: x ** 2, (list(filter(lambda x: x % 2 == 0, lst))))))

# list comprehensions
new_lst2 = []
[new_lst2.append(randint(1, 10)) for i in range(5)]
print(new_lst2)

sqrs_exps = [x ** 2 for x in lst if x % 2 == 0]
print(sqrs_exps)

next_lst = list(randint(1, 10) for x in range(10))
print(next_lst)
