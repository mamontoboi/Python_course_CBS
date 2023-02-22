# The method __eq__ is used when == is called to make objects equal if they have same value of required parameter.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):  # isinstance is used to determine whether the object belongs to the class Person
            return self.age == other.age  # __eq__ returns True if 2nd object has same age as 1st object

        return False  # returns False if object doesn't belong to the class Person (doesn't have age attribute)


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

print(john == jane)  # True, because both are 25
print(john == mary)  # False


john = Person('John', 'Doe', 25)
print(john == 20)  # False, because 20 is not Person