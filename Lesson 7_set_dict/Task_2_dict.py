# Створіть програму, яка емулює роботу сервісу зі скорочення посилань. 
# Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового 
# посилання за її назвою.

import re

url = input(r'Paste your URL here or write "stop": ')
dct = {}

while url != 'stop':
    ident = ''.join(re.findall('https://([\S]+?)/', url))
    dct[ident] = url
    url = input(r'Paste your URL here or write "stop": ')
    continue

print("This is a list of pages in the DB: \n", dct.keys())
req = input("What do you want to open? \n")
if req in dct.keys():
    print(f"This is the URL you desired: {dct[req]}")
else:
    print("The URL you entered is not in the DB")


