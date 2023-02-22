# Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє арифметичне,
# і головного циклу, що запитує у користувача числа і обчислює їх середні значення за допомогою створеної функції.


def mean_value(*args):
    i, total = 0, 0
    for n in args:
        i += 1
        total += n
    return f'The mean value of given figures is {total / i}'


def main():
    print(mean_value(int(input("Enter a = ")), int(input("Enter b = ")), int(input("Enter c = "))))


if __name__ == '__main__':
    main()
