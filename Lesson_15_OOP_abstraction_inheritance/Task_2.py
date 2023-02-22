# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_ast(self):
        for _ in range(self.length):
            print('*  ' * self.width)
        print()


class Button:
    @staticmethod
    def click_button():
        print("click")
        x = Rectangle.__new__(Rectangle)
        x.__init__(5, 7)
        x.print_ast()


sq = Rectangle(5, 10)
sq.print_ast()

mouse_left_button = Button

mouse_left_button.click_button()