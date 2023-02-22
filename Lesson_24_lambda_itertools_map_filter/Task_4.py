# Створіть звичайну функцію множення двох чисел. Створіть каррувану функцію множення двох чисел.
# Частково застосуйте її до одного аргументу, до двох аргументiв

def mult(a, b):
    return a * b


def currying_mult(a):
    def another_fig(b):
        return a * b
    return another_fig


print(currying_mult(2)(3))

another_arg = currying_mult(2)
print(another_arg(3))
