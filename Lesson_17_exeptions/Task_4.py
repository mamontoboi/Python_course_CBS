# Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення,
# і перехопіть цей виняток під час виклику функції.

class ExpectUnexpected(Exception):
    def __str__(self):
        return f'In the ideal world a salary raise cannot be negative'


def is_positive(val):
    if val > 0:
        return val
    else:
        raise ExpectUnexpected(val)


def init_check():
    while True:
        try:
            quest = input("State the salary raise: ")
            quest = int(quest)
        except ValueError as ve:
            print(ve)
            continue
        else:
            print(is_positive(quest))
        finally:
            print("All checks have been completed")


if __name__ == '__main__':
    init_check()
