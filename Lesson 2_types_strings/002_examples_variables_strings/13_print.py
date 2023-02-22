# Вказуємо роздільник
from functools import partial

print(2, 3, 5, 7, 9, sep='; ')
# він може бути і порожнім рядком
print('he', 'llo', sep='')

# Вказуємо кінець рядка
print(1, end=' ')
# два переводи каретки після рядка
print(2, end='\n\n')
# порожній кінець
print('he', end='')
print('llo')

print(print(1))
print(len("123"))

print_partial = partial(print, sep='+')  # from functools import partial => 1+2+3+4
print_partial(1, 2, 3, 4)
