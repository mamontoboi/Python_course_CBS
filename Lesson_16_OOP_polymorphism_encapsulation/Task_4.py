# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно
# "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.

class Base:
    @classmethod
    def say_hi(cls):
        print(f"Hello from", cls.__name__)


class Child(Base):
    pass

parent = Base()
parent.say_hi()

kinder = Child()
kinder.say_hi()
