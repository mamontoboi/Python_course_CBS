import re
import shelve


def display_database(db, name_of_file='Task_1_database'):
    with shelve.open(name_of_file, 'c') as db:
        for key in db.keys():
            print('\t', key)


def append_database(db, name_of_file='Task_1_database'):
    with shelve.open(name_of_file, 'c') as db:
        url = input(r'Paste your URL, starting with https://, here, or write "stop": ')
        while url != 'stop':
            ident = ''.join(re.findall('https://(\S+?)/', url))
            db[ident] = url
            url = input(r'Paste your URL, starting with https://, here, or write "stop": ')
            continue
    return db


def find_link(db, name_of_file='Task_1_database'):
    display_database(db)
    with shelve.open(name_of_file, 'c') as db:
        while True:
            req = input("What link do you want to examine? \n")
            try:
                print(db[req])
                break
            except KeyError:
                print(f"The key {req} is not in the database")
                continue


def del_entry(db, name_of_file='Task_1_database'):
    display_database(db)
    with shelve.open(name_of_file, 'c') as db:
        while True:
            req = input("What link do you want to delete? \n")
            try:
                del db[req]
                break
            except KeyError:
                print(f"The key {req} is not in the database")
                continue
