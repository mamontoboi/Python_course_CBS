# Використовуючи код з завдання 2, використати функції hassttr(), getattr(), setattr(), delattr().

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


john = Contact('Kennedy', 'John', 45, '+1234567890', 'jfk@potus.com')
bob = UpdateContact('Kennedy', 'Robert', 40, '+1234567890', 'bob@senat.com', 'senator')

# john.send_message()

# bob.get_message()

print(hasattr(john, 'name'))  # True

print(getattr(john, 'name'))  # John

setattr(john, 'name', 'Fitzgerald')
print(getattr(john, 'name'))  # Fitzgerald

delattr(john, 'name')
print(john.__dict__)  # {'surname': 'Kennedy', 'age': 45, 'mob_phone': '+1234567890', 'email': 'jfk@potus.com'}