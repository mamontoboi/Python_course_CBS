class GetAttribute1:
    # атрибут класу GetAttribute1
    my_attr1 = 1

    def __init__(self):
        # атрибут екземпляру класу GetAttribute1
        self.my_attr2 = 2

    # __getattr__ called only when attr NOT in the class
    def __getattr__(self, my_attr):
        # Не attr1: наслідується від класу
        # Не my_attr2: зберігається у екземплярі
        print('Get: ' + my_attr)
        return "Not in the class"


A = GetAttribute1()
print(A.my_attr1)  # 1
print(A.my_attr2)  # 2
print(A.my_attr3)  # Get: my_attr3 / Not in the class

A.my_attr4 = 6
print(A.my_attr4)  # 6

# Off-top!
print(A.__dict__)  # {'my_attr2': 2, 'my_attr4': 6}. my_attr1 not in the dict!
print(GetAttribute1.__dict__)  # {'..., 'my_attr1': 1, ...}. 2 and 4 are not in the dict

print('-' * 50)


class GetAttribute2(object):
    my_attr1 = 1

    def __init__(self):
        self.my_attr2 = 2

    # __getattribute__ called EVERY TIME by default
    def __getattribute__(self, my_attr):
        # Для запобігання зацикленню використовується суперклас
        print('Get: ' + my_attr)
        if my_attr == 'my_attr3':
            return "my_attr3 is not in the class"
        else:
            print(f"getting {my_attr}")
            return object.__getattribute__(self, my_attr)  # supermethod, reference to superclass object. Error.


B = GetAttribute2()
print(B.my_attr1)
print(B.my_attr2)
print(B.my_attr3)
# Незважаючи на те, що метод __getattribute__ перехоплює більше операцій звернення до атрибутів, ніж метод __getattr__,
# проте на практиці вони виявляються лише варіаціями на одну тему - якщо атрибути фізично не зберігаються в пам'яті,
# ці два методи дають один і той самий ефект - AttributeError.
print(B.my_attr4)
