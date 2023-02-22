from collections import namedtuple

# Іменований кортеж
Person = namedtuple('Person', 'name surname')
named_tuple = Person('Іван', 'Іванов')
print(named_tuple)

Person(name='Іван', surname='Іванов')
print(named_tuple[0])
print(named_tuple[1])
named_tuple = named_tuple._replace(surname='JJJ')
print(named_tuple)

