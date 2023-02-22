# Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact.

class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def __str__(self):
        return {self.name}, {self.surname}, {self.age}, {self.mob_phone}, {self.email}

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

    def __str__(self):
        return {self.name}, {self.surname}, {self.age}, {self.mob_phone}, {self.email}, {self.job}


class NewClass:
    pass


class HybridClass(NewClass, Contact):
    pass


print(dir(Contact))

