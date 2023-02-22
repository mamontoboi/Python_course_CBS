my_set = {1, 2, 3}
print(my_set)
# {1, 2, 3}

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
# {1.0, (1, 2, 3), 'Hello'}
# my_set2 = {1, 2, 3, {4, 5}, 6, 7}
# print(my_set2)  # Error. Set cannot contain unhashable items, such as list, dict and sets themselves.
# my_set = {1, 2, [3, 4, 5]}
# print(my_set)  # Error. Set cannot contain unhashable items, such as list, dict and sets themselves.
my_var = {1}
print(my_var)
my_var = set()
print(my_var)

