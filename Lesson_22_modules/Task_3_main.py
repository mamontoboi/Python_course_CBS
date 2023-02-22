# Створіть модуль для отримання простих чисел. Імпортуйте його з іншого модуля. Імпортуйте його окремі імена.
import Task_3_engine as engine
from Task_3_engine import *
# or
# from Task_3_engine import prime_gen, x


if __name__ == '__main__':
    cnt = 0
    qnt = engine.inquire()
    while cnt < qnt:
        i = (next(engine.prime_gen()))
        if (i == 2 or i == 3 or i == 5) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0) and i != 1:
            print(i)
            cnt += 1


print(x)


