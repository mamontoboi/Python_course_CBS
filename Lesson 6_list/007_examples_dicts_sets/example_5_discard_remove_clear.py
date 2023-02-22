# Різниця між discard() та remove()

# Створення множини
my_set = {1, 3, 4, 5, 6}
print(my_set)

# Виключення елемента
# Виведення: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# Видалення елемента
# Виведення: {1, 3, 5}
my_set.remove(6)
print(my_set)

# Виключення елемента, якого немає в множині
my_set.discard(2)  # Виведення: {1, 3, 5}
print(my_set)

# Виключення елемента, якого немає в множині

# my_set.remove(2)  # Виведення: KeyError

my_set.clear()
print(my_set)
