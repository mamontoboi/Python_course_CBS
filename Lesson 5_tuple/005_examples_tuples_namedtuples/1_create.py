my_tuple = (1, 2, 3)

print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[2])  # same as
print(my_tuple.__getitem__(2))
print(my_tuple[-1])  # same as
print(my_tuple.__getitem__(-1))

