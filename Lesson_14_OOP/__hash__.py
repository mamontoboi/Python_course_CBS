# The method __hash__ is used when it is necessary to make object hashable after implementation of __eq__ method.
# Unhashable (mutable) objects cannot be keys in dictionary or elements in sets. This can be fixed with __hash__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property  # to make age attribute immutable
    def age(self):
        return self._age

    def __eq__(self, other):  # __eq__ is specified to make comparisons, e.g. by age
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):  # __hash__ is introduced to make an object of the class hashable
        return hash(self.age)

# without __hash__ Persons couldn't be a set items
members = {
    Person('John', 22),
    Person('Jane', 22)
}