print("ax^2 + bx + c = 0")
print('Please enter the following coefficients')
a = float(input('Please enter a: '))
b = float(input('Please enter b: '))
c = float(input('Please enter c: '))

D = b ** 2 - 4 * a * c

print(D)

x1 = (-b + D**0.5) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)

print(complex(x1, x2))