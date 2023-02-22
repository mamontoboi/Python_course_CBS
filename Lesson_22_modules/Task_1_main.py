# Перепишіть домашнє завдання попереднього уроку (сервіс для скорочення посилань) таким чином,
# щоб у нього була основна частина, яка відповідала би за логіку роботи та надавала узагальнений інтерфейс,
# і модуль представлення, який відповідав би за взаємодію з користувачем.
# При заміні останнього на інший, який взаємодіє з користувачем в інший спосіб, програма має продовжувати
# коректно працювати.

import shelve
import Task_1_func as func

db = None


def start():
    global db
    with shelve.open('Task_1_database', 'c') as db:
        db['python_doc'] = 'https://docs.python.org/3/library/shelve.html'
        db['csb_home_tasks'] = 'https://lms.cbs.com.ua/mod/assign/view.php?id=1167'
    print("This is a list of pages in the DB:")
    func.display_database(db)


def interaction():
    while True:
        action = input("Please choose on of the following actions:\n\t"
                       "Press 1 to check the contents of database \n\t"
                       "Press 2 to add the link to the database \n\t"
                       "Press 3 to find the corresponding link \n\t"
                       "Press 4 to delete the entry \n\t"
                       "Write 'off' for exit \n").lower()
        match action:
            case '1':
                func.display_database(db)
            case '2':
                func.append_database(db)
            case '3':
                func.find_link(db)
            case '4':
                func.del_entry(db)
            case 'off':
                print("Thank you for using our database. Good bye!")
                break
            case _:
                print("Wrong entry! Try again.")
                continue


if __name__ == '__main__':
    print("Welcome to our database!")
    start()
    interaction()



