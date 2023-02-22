# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел.
# Створіть ще один скрипт, який читає числа з файлу та виводить на екран їхню суму.

from random import randint


def number_gen():
    yield randint(0, 1000)


with open("task_1.txt", mode='w', encoding='utf-8') as fh:
    for _ in range(10000):
        fh.write(str(next(number_gen())) + '\n')

# fh = open("task_1.txt", mode='r', encoding='utf-8')
# print(fh.read())
# fh.close()

with open("task_1.txt", mode='r+', encoding='utf-8') as fh:
    for line in fh:
        total = sum(map(int, fh))
    print(total)
