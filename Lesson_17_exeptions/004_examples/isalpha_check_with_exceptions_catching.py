class NotLetters(Exception):
    def __str__(self):
        return f'Must contain only letters!'


def check_letters(value):
    try:
        if value.isalpha():
            print("Only letters here!")
            return value
        else:
            raise NotLetters
    except NotLetters as e:
        print(f'{e.__class__}: {e}')


check_letters(input('Write: '))
