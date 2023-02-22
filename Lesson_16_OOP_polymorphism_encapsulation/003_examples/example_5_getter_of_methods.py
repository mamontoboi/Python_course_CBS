# example_5.py
class Test:
    def __init__(self, test_value):
        self.__private_attr = test_value

    def get_private_attr(self):
        return self.__private_attr

    def set_private_attr(self, value):
        self.__private_attr = value

    @staticmethod
    def __private_function():
        print("I'm private")

    def call_private(self):  #getter
        self.__private_function()


test = Test(test_value=15)
print(test.get_private_attr())  # 15. It was submitted during class instantiation
test.set_private_attr(35)
print(test.get_private_attr())  # 35
test.call_private()  # I'm private

