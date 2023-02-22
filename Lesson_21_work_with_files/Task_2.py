# Створіть програму, яка емулює роботу сервісу зі скорочення посилань. 
# Повинна бути реалізована можливість введення початкового посилання та короткої назви і отримання початкового 
# посилання за її назвою.

# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так,
# щоб він зберігав базу посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з модулем
# shelve (https://docs.python.org/3/library/shelve.html), який у даному випадку буде дуже зручним та спростить
# виконання завдання.

import re
import shelve


sh = shelve.open('links_db', 'c')
sh['python_doc'] = 'https://docs.python.org/3/library/shelve.html'
sh['csb_home_tasks'] = 'https://lms.cbs.com.ua/mod/assign/view.php?id=1167'
url = input(r'Paste your URL, starting with https://, here, or write "stop": ')
while url != 'stop':
    ident = ''.join(re.findall('https://(\S+?)/', url))
    sh[ident] = url
    url = input(r'Paste your URL, starting with https://, here, or write "stop": ')
    continue


print("This is a list of pages in the DB:")
for key in list(sh.keys()):
    print(key)
while True:
    req = input("What link do you want to examine? \n")
    try:
        print(sh[req])
        break
    except KeyError:
        print(f"The key {req} is not in the database")
        continue
sh.close()
