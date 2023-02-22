class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

    @classmethod  # class method is used to create new instance just by calling the method (without providing data)
    def create_anonymous(cls):
        return Person('John', 'Doe', 25)


anonymous = Person.create_anonymous()
print(anonymous.introduce())
