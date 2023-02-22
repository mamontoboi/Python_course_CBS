# reversed дозволяє перебирати послідовність у зворотному порядку:
for i in reversed({'key': 'value', 'ley': 'pey'}.keys()):
    print(i)

for i in reversed((1, 2, 3, 4)):
    print(i)

for i in reversed([1, 2, 3, 4]):
    print(i)

for i in reversed('word'):
    print(i)

# for i in reversed({1, 2, 3, 4}):  # TypeError: 'set' object is not reversible
#     print(i)

# for i in reversed(1):  # TypeError: 'int' object is not reversible
#     print(i)