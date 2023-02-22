a, b, c = 1, 2, 3
# міняємо місцями значення двох змінних:
my_tuple = 10, 50, 90
a, b = b, a
a, b, c = my_tuple
print(a, b, c)

head, *tail = my_tuple
print(head)

print(tail)
print(*tail)

for index, value in enumerate(my_tuple):
    print(index, value)
