"""
У цьому прикладі розглядаються документаційні рядки
"""


def function():
    """
    Рядок, що стоїть на самому початку функції (а також модуля, класу або методу),
    грає роль особливого виду коментарів – документаційного рядка (docstring).
    """
    print('function called\n\n')


# Виклик функції
function()

# Виведення документаційного рядка на екран.
# Після імені функції немає круглих дужок, тому вона не викликається,
# а сама розглядається як певний об'єкт
print(function.__doc__)

# Функція help служить для виведення довідки
help(function)  # виклик довідки за певною користувачем функції
help(print)  # виклик довідки щодо стандартної функції
