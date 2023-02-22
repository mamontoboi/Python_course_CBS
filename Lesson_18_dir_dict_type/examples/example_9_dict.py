class MyClass:
    """
    Some text
    """
    my_field = 1
    my_field2 = 2

    def __init__(self):
        self.a = "1"


print(MyClass.__dict__)
# {'__module__': '__main__', '__doc__': '\n    Some text\n    ', 'my_field': 1, 'my_field2': 2, '__init__':
# <function MyClass.__init__ at 0x0000027AE1448D60>, '__dict__': <attribute '__dict__' of 'MyClass' objects>,
# '__weakref__': <attribute '__weakref__' of 'MyClass' objects>}

print(dir(MyClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', 'my_field', 'my_field2']