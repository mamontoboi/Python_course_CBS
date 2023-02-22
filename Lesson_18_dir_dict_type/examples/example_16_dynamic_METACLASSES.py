# class Foo:
#     bar = "blablabla"

#  same as:

# Creation of the class Foo
Foo = type('Foo', (), {'bar': "blablabla"})
# <class 'type'>
print(type(Foo))
# {'bar': 'blablabla', '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
# <class 'type'>
print(Foo.__dict__)

# <class 'type'>
print(Foo.__class__)

# Класс Foo, созданный через метакласс type() можно использовать как обычный класс:
# <class '__main__.Foo'>
print(Foo)

f = Foo()
# blablabla
print(f.bar)


# можно наследоваться от него
class FooChild(Foo):
    pass
# <class '__main__.FooChild'>
print(FooChild())
# bar унаследован от Foo
# blablabla
print(FooChild.bar)
# Добавим методы в класс FooChild(). Для этого определим функцию и добавим ее как атрибут.

def echo_bar(self):
    print(self.bar)


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
# False
hasattr(Foo, 'echo_bar')
# True
hasattr(FooChild, 'echo_bar')

my_foo = FooChild()
print(my_foo)
my_foo.echo_bar()
# blablabla
print(my_foo)

# после динамического создания класса добавим еще один метод


def echo_bar_more(self):
    print('yet another method')


FooChild.echo_bar_more = echo_bar_more
hasattr(FooChild, 'echo_bar_more')
# True
