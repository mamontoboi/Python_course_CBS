# Створити клас Contact з полями surname, name, age, mob_phone, email.
# Додати методи get_contact, sent_message. Створити клас UpdateContact з полями surname, name, age, mob_phone, email, job.
# Додати методи get_message. Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів:
# __dict__, __base__, __bases__. Роздрукувати інформацію на екрані.

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f'{self.name} {self.surname} has number {self.mob_phone}, email {self.email}'

    def send_message(self):
        if self.surname == input("Write the surname: "):
            print(f"Ready to send the message to {self.name} {self.surname}")
        else:
            print("Not found")
            Contact.send_message(self)


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        print(f"This is your message from {self.name} {self.surname}")


class NewClass:
    pass


class HybridClass(NewClass, Contact):
    pass


john = Contact('Kennedy', 'John', 45, '+1234567890', 'jfk@potus.com')
bob = UpdateContact('Kennedy', 'Robert', 40, '+1234567890', 'bob@senat.com', 'senator')

# john.send_message()

# bob.get_message()

print(Contact.__dict__)  # {'__module__': '__main__', '__init__': <function Contact.__init__ at 0x000002367267C680>,
# 'get_contact': <function Contact.get_contact at 0x0000023672A79940>, 'send_message': <function Contact.send_message
# at 0x0000023672AA1DA0>, '__dict__': <attribute '__dict__' of 'Contact' objects>, '__weakref__': <attribute '__weakref_
# _' of 'Contact' objects>, '__doc__': None}
print()
print(Contact.__base__)  # <class 'object'>
print()
# print(Contact.__bases_)  # Traceback. Type object 'Contact' has no attribute '__bases_'
print()
print(UpdateContact.__dict__)   # {'__module__': '__main__', '__init__': <function UpdateContact.__init__ at
# 0x0000023672AA25C0>, 'get_message': <function UpdateContact.get_message at 0x0000023672AA2660>, '__doc__': None}
print()
print(UpdateContact.__base__)  # <class '__main__.Contact'>
print()
# print(UpdateContact.__bases_)  # Traceback. Type object 'UpdateContact' has no attribute '__bases_'
print()
print(john.__dict__)  # {'surname': 'Kennedy', 'name': 'John', 'age': 45, 'mob_phone': '+1234567890',
# 'email': 'jfk@potus.com'}
print()
# print(john.__base__)  # Traceback. 'Contact' object has no attribute '__base__'
print()
# print(john.__bases_)  # Traceback. 'Contact' object has no attribute '__bases_'
print()
print(bob.__dict__)  # {'surname': 'Kennedy', 'name': 'Robert', 'age': 40, 'mob_phone': '+1234567890',
# 'email': 'bob@senat.com', 'job': 'senator'}
print()
# print(bob.__base__)  # Traceback. 'UpdateContact' object has no attribute '__base__'
print()
# print(bob.__bases_)  # Traceback. 'UpdateContact' object has no attribute '__bases_'
print(dir(john))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'age', 'email', 'get_contact', 'mob_phone', 'name', 'send_message', 'surname']
print()
print(HybridClass.__bases__)  # (<class '__main__.NewClass'>, <class '__main__.Contact'>)


