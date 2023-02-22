# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор:
# твір. Передбачте можливість виведення на екран сортування за автором та твором.
from operator import itemgetter

library = {}
key = input("Please write the name of the authon:\n").title()
val = input("Please write the name of his book:\n")
library[key] = val

while key != 'Stop':
    print(library)
    key = input("Please write the name of the authon or write 'Stop'.\n").title()
    if key == 'Stop':
        break
    library[key] = input("Please write the name of  his book.\n")

act = input("How do you want to sort the libraty: \n\tby author \n\tby book \n").lower()

if act == 'by author':
        sort_by_author = sorted(library)
        print("The library sorted by author's name: \n", sort_by_author)
elif act == 'by book':
        sort_by_book = sorted(library.items(), key=itemgetter(1))
        print("The library sorted by the names of the books: \n", sort_by_book)