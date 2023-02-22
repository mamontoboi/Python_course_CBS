# Створіть магазин канцтоварів використовуючи списки для зберігання елементів.
# Для додавання елементів створіть функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу
# додавати у створений список на початку. Результат вивести на екран.
# Під час створення дотримуйтесь правил специфікації PEP 8.

lst_of_elements = []

while True:
    choise = input("Do you want to add some stationary items? Yes/No\n").lower()
    if choise not in ('yes', 'y'):
        break
    elements = []
    while True:
        element = input("Write an item's name or write 'quit': ")
        if element == 'quit':
            break
        elements.append(element)
    lst_of_elements.insert(0, tuple(elements))
    print(f'Presently list of stationary items in your stock is the following: \n{lst_of_elements}')

print(f'This is a final list of all items that are in your stock: \n{lst_of_elements}')
