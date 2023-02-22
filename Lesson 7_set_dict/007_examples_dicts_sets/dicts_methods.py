my_dict = {'key': 'value', 10: True, 0.2: "hello"}
print(my_dict)
print(my_dict.get('key2', -1))  # look for the key in dict. -1 if not found
print(my_dict)

d = {1: 10, 2: 20}
print(d.items())
d.clear()
print(d)
d = {"1": "world", "2": "a"}
print(1)
print(d.popitem())
print(d)
d = {1: 3, 2: 4, 5: 2}
d1 = {55: 6, 45: 3}
d.update(d1)
print(d)
print(d.values())

d = {1: 3, 2: 4, 5: 2}
d1 = {5: 6, 6: 3}
d.update(d1)  # if two dicts have the same key, only key-value of last dict will remain
print(d)  # {1: 3, 2: 4, 5: 6, 6: 3}

d2 = d.copy()
print(d2)
