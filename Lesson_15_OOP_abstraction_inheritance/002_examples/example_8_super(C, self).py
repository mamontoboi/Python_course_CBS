# Функція super(). Множинне успадкування
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('sub_method from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('sub_method from class C:', b)
        super().sub_method(b + 1)


class D(C):
    def __init__(self):
        print('Initializing: class D')
        # super() з параметрами
        super(C, self).__init__()  # refers to parental class to method C, not to D
        """super() looks for a stated method (__init__ in this case) in superclass of stated class.
        In case super(C, self) will look for init in B class. By default, super(), would be searching in C.  
        """
    def sub_method(self, b):
        print('sub_method from class D:', b)
        super().sub_method(b + 1)


c = C()
c.sub_method(1)
print('Зверніть увагу як відбувається ініціалізація')
print('класів при вказівці аргументів у функції super()')
d = D()
d.sub_method(1)
