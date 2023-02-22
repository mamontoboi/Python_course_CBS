class MyClass1:
    """Some text"""
    # __slots__ - Дозволяє знизити обсяг пам'яті, споживаної екземплярами класу, обмежуючи кількість атрибутів, що ними
    # підтримуються. За замовчуванням класи використовують словник для зберігання атрибутів - це дозволяє модифікувати
    # набір атрибутів об'єкта безпосередньо під час виконання програми.
    __slots__ = []
    my_var1 = 'text'
    my_var2 = 21


print(MyClass1.__dict__)


class MyClass2:
    """Some text"""
    # __slots__ - Дозволяє знизити обсяг пам'яті, споживаної екземплярами класу, обмежуючи кількість атрибутів, що ними
    # підтримуються. За замовчуванням класи використовують словник для зберігання атрибутів - це дозволяє модифікувати
    # набір атрибутів об'єкта безпосередньо під час виконання програми.
    my_var1 = 'text'
    my_var2 = 21
    # Спеціальний атрибут __slots__ дозволяє вам явно вказати, які атрибути екземпляра ви очікуєте від екземплярів
    # вашого об'єкта, з очікуваними результатами:
    # - швидкий доступ до атрибутів.
    # - економія пам'яті.
    # Місце заощаджується тому що:
    # - Посилання зберігаються на значення слотів, а не в __dict__
    # - Заборона створення __dict__ та __weakref__, якщо батьківські класи забороняють їх, і ви оголошуєте __slots__.
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


m_c = MyClass2(1, 2, 3)
# print(m_c.__slots__)
print(dir(m_c))
from sys import getsizeof
print(getsizeof(MyClass1()), getsizeof(m_c))

# Сверху херовый пример. А вот нормальный:

class Ordinary(object):
    """Экземпляры этого класса могут дополняться атрибутами
    во время исполнения.

    """


class WithSlots(object):
    __slots__ = 'static_attr'


a = Ordinary()
b = WithSlots()

a.__dict__  # {}
# b.__dict__  # AttributeError

a.__weakref__  # None
# b.__weakref__  # AttributeError

a.static_attr = 1
b.static_attr = 1

a.dynamic_attr = 2
# b.dynamic_attr = 2  # AttributeError
# So, if __slots__ = 'static_attr' is stated only one attribute can be added. Not infinite quantity as usual in dictionary.
