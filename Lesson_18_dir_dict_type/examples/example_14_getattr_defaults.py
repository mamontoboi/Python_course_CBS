class MyClass:
    name = 'Dmytro Dmytrenko'
    phone = '+380669480103'
    country = 'Ukraine'


x = getattr(MyClass, 'phone')
print(x)
# +380669480103

# Видалимо атрибут phone з об'єкта MyClass:
delattr(MyClass, 'phone')

# Спробуємо отримати атрибут phone з об'єкта MyClass:
# x = getattr(MyClass, 'phone')
# print(x)  # AttributeError: type object 'MyClass' has no attribute 'phone'

# Спробуємо отримати атрибут phone з об'єкта MyClass:
x = getattr(MyClass, 'phone', '+380951850809')
print("NEW:", x)
