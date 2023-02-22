# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

import json as j


def reversed(iter_obj):
    rev = []
    while True:
        try:
            element = next(iter_obj)
            rev.insert(0, element)
        except StopIteration:
            break
    return rev


iterable = range(10)

iter_obj = iter(iterable)

print(reversed(iter_obj))


json.dump(iter_obj)