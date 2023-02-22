class A:
    """Some text"""
    x = 1

    def b(self):
        print(self.__dict__, "\n")
        print(dir(self))


a = A()
# a.b()
# print()
print(A.__dict__)  # {'__module__': '__main__', '__doc__': 'Some text', 'x': 1, 'b': <function A.b at 0x000001F65E07A020>,
# '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>}  -- data
print()
print(a.__dict__)  # {}  -- pairs of attrs and value, if any
print()
print(dir(a))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'b', 'x']  --- available methods. same as class methods

print(dir(A))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'b', 'x']
