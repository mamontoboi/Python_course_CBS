# Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не вважається простим.
# Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран,
# а потім на вимогу користувача виводить їхню суму або добуток.
import math

a = int(input("Please state the starting point of the range: "))
b = int(input("Please state the end point of the range: "))
prime_number_lst = []

for element in range(a, b + 1):
    if element % 2 == 0 or element % 3 == 0 or element % 5 == 0 or element == 1:
        continue
    else:
        prime_number_lst.append(element)

print(f"The numbers {prime_number_lst} in the range are prime numbers. ")
dec = input("If you want to find SUM press 1. \nIf you want to find the PRODUCT press 2. \n")
match dec:
    case '1':
        print(sum(prime_number_lst))
    case '2':
        print(math.prod(prime_number_lst))
