# Створення списку
my_list = [1, 3, 6, 10]

# піднести кожен елемент до квадрату, використовуючи спискове включення
list_ = [x ** 2 for x in my_list]

# подібний механізм із генераторами:
# Вирази генератора укладені в круглі дужки ()
generator = (x ** 2 for x in my_list)

print(list_)  # [1, 9, 36, 100]
print(generator)  # <generator object <genexpr> at 0x000001A1EDFCC040>
print(list(generator)) # [1, 9, 36, 100]
