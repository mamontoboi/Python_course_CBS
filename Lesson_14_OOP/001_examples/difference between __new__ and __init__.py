class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre


#  when actions of new not specified. Just default creation of new object
kng = object.__new__(Book)
print(kng.__dict__)  # {}. Because object was created, but not processed

kng.__init__('King', 'It', '1986', 'horror')  # init method processed the data
print(kng.__dict__)  # {'author': 'King', 'title': 'It', 'year': '1988', 'genre': 'horror'}.


class SquareNumber(int):
    def __new__(cls, value):
        return super().__new__(cls, value ** 2)  # inheritance from the in-built type 'int'


x = SquareNumber(3)
print(x)  # 9
print(isinstance(x, int))  # True


# __new__ method can replace __init__ method and modify the object during creation
class Person:
    def __new__(cls, first_name, last_name):
        # create a new object
        obj = super().__new__(cls)  # this must be specified because default method __new__ has been changed

        # initialize attributes
        obj.first_name = first_name
        obj.last_name = last_name

        # inject new attribute
        obj.full_name = f'{first_name} {last_name}'
        return obj  # this must be specified because default method __new__ has been changed


person = Person('John', 'Doe')
print(type(person))  # <class '__main__.Person'>
print(person.full_name)  # John Doe

print(person.__dict__)  # {'first_name': 'John', 'last_name': 'Doe', 'full_name': 'John Doe'}