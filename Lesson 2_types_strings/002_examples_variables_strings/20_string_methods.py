string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Поділ рядка поелементний, при цьому створюється список
print(string.split())  # ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipisicing', 'elit.']

print(string.strip())  # Lorem ipsum dolor sit amet, consectetur adipisicing elit.  - removes spaces at both sides
print(string.count('s'))  # 4
print(string.replace('Lorem', 'LOREM'))  # LOREM ipsum dolor sit amet, consectetur adipisicing elit.

print(str(len(string)).isdigit())  # True
print(string.title())  # Lorem Ipsum Dolor Sit Amet, Consectetur Adipisicing Elit.
print(string.capitalize())  # Lorem ipsum dolor sit amet, consectetur adipisicing elit.  -- first letter on sentence
print(string.lower())
print(string.upper())
print(string.center(100, '+'))  # +++++++++++++++++++++Lorem ipsum dolor sit amet, consectetur adipisicing elit. +++++++++++++++++++++
my_char = ord(string[0])  # ASCII number of symbol
print(my_char)  # 76
print(chr(my_char))  # L
print('\nstring'.isspace())     #  Return True if the string is a whitespace string, False otherwise.
print(string.startswith('L'))  # True
print(string.endswith('.'))  # True
print('string'.isalpha())  # True --  Return True if the string is an alphabetic string -- letters
print('string'.isalnum())  # True --  Return True if the string is an alpha-numeric string -- letters and numbers
print('string'.isdigit())  # False --  Return True if the string is a digit string -- numbers
print(string.casefold())  # lorem ipsum dolor sit amet, consectetur adipisicing elit.
