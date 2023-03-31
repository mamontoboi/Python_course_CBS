# Напишіть функцію-генератор для отримання n перших простих чисел.

def gen(val):
    for i in range(val + 1):
        if i == 2 or i == 3 or i == 5 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0):
            yield i


print(list(gen(300)))

rng = 500

print(list(i for i in range(rng) if i == 2 or i == 3 or i == 5 or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0)))
