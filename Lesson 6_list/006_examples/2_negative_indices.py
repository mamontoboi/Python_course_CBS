# Також можна використовувати негативні індекси.
# У такому випадку обхід елементів починається не з першого, а з останнього.
# Індекс останнього елемента списку -1,
# Передостаннього - -2 і т.д.

# Створення списку чисел
my_list = [5, 7, 9, 1, 10, 2]

# Отримання передостаннього значення
pre_last = my_list[-2]  # pre_last == 1
print(pre_last)

# Обчислення суми першого та останнього значень
result = my_list[0] + my_list[-1]
print(result)
