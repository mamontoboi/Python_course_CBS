class MyClass:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.age}'


print(dir(MyClass("Petrenko", "Dmytro", 20)))

# Без рефлексії
m_c = MyClass("Petrenko", "Dmytro", 20)
print(m_c.__str__())  # Petrenko, Dmytro, 20
print(m_c.__dict__)  # {'surname': 'Petrenko', 'name': 'Dmytro', 'age': 20}
print(m_c.__class__)  # <class '__main__.MyClass'>
print(type(m_c))  # <class '__main__.MyClass'>


# З рефлексією
class_name = "MyClass"
method = "__str__"
# The globals() method returns the dictionary of the current global symbol table
print("\nDictionary of the current global symbol table:", globals())
m_c = globals()[class_name]("Petrenko", "Dmytro", 20)
print(getattr(m_c, method)())

# З eval
print(eval("MyClass(\"Petrenko\", \"Dmytro\", 20).__str__()"))
