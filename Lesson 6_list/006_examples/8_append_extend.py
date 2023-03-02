# Створення порожнього списку
my_list = list()

# Метод append додає значення до списку
my_list.append(3)
my_list.append(5)
my_list.append(my_list[0] + my_list[1])

# Виведення списку на екран
print(my_list)

# Додавання кількох елементів до кінця списку
c = (93, 100, 91)
my_list.extend(c)
print(my_list)

# [3, 5, 8, 93, 100, 91, 'a', 'd', 'd']
c = 'add'
my_list.extend(c)
print(my_list)

# [3, 5, 8, 93, 100, 91, 'a', 'd', 'd', 'add']
my_list.append(c)
print(my_list)
