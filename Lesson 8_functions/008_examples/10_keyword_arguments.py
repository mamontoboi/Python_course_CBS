# Функція, яка приймає три аргументи
def info(obj, color, price):
    print('Об\'єкт:', obj)
    print('Колір:', color)
    print('Ціна:', price)
    print()


# передача параметрів у прямому порядку
info('ручка', 'синій', 1)

# передача параметрів у довільному порядку
info(price=5, obj='чашка', color='помаранчевий')

# можна змішувати обидва способи, але спочатку повинні йти параметри, які передаються у прямому порядку
info('кава', price=10, color='чорний')
