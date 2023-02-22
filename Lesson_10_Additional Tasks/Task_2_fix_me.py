from math import pi, e

numb = 5

cnt = int(input('\tВведите количество повторов : '))

print(cnt)
print(pi * numb * cnt)
print(e * 2)

while numb >= 0:
    numb -= 1

word = 'my string'
total = 0

for elem in word:
    total += pow(word.find(elem), 2)

print("sum =", total)


def my_func(atr=1):
    print("\tatr: ", atr)


my_func(atr=5)
