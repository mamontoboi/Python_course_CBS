def function(x):
    """
    Ця функція повертає аргумент, помножений на два, якщо він негативний, або аргумент,
    помножений на три, якщо він більший або дорівнює нулю
    """
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    """
    Виведення значень функції у діапазоні [-3, 3]
    """
    for i in range(-3, 4):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


if __name__ == '__main__':
    main()
