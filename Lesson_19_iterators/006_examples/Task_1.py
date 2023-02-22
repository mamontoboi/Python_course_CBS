# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable

iterable = iter(range(1, 101))

for i in iterable:
    print(i)


def letters_range(a, b):
    """This function generates the alphabet"""
    for j in range(ord(a), ord(b)+1):
        yield chr(j)


lst = []
for i in letters_range('a', 'z'):
    lst.append(i)

lst = iter(lst)

while True:
    try:
        print(next(lst))
    except StopIteration:
        break


