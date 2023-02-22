# Створіть програму, яка має 2 списки цілочисельних значень та друкує список унікальних значень
# без повтору, які є в 1 списку (немає в другому) і навпаки.

import random

list_1, list_2 = [], []
n = random.randint(10, 20)
m = random.randint(10, 20)

for _ in range(n):
    list_1.append(random.randint(0, 1000))
for _ in range(m):
    list_2.append(random.randint(0, 1000))

set_1, set_2 = set(list_1), set(list_2)

print("This is the list of unique values of both initial lists: {}".format(list(set_1.symmetric_difference(set_2))))