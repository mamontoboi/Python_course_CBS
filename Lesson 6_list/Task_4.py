# Створіть список, введіть кількість його елементів і самі значення.
# Передбачити меню, в якому: після натискання клавіші 1 ці значення виведуться на екран у зворотному порядку,
# а після натискання клавіші 2 – за зростанням.

import random

quantity = int(input("How many numbers do you want to obtain? "))
rng_lst = []

for _ in range(quantity):
    rng_lst.append(random.randrange(-1000, 1000))

given_choice = input("How do you want to sort them: \n\t1 - in reversed order \n\t2 - in ascending order "
                     "\n\t3 - in descending order \n")

match given_choice:
    case '1':
        rng_lst.reverse()
        print(f"Reversed list: {rng_lst}")
    case '2':
        print(f"List sorted in ascending order: {sorted(rng_lst)}")
    case '3':
        print(f"List sorted in ascending order: {sorted(rng_lst, reverse=True)}")

