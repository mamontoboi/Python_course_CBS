# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
# Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих
# двох об'єктів в одній функції (функція hello_friend).
class Language:
    def __init__(self, name):
        self.name = name


class LenguaCastellana(Language):
    def greeting(self):
        print(f'!Bienvenido, {self.name}!')


class English(Language):
    def greeting(self):
        print(f'Welcome, {self.name}!')


def hello_friend(*args):
    for i in args:
        i.greeting()


jorge = LenguaCastellana('Jorge')
john = English('John')

hello_friend(jorge, john)
