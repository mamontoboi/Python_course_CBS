# Є рядок, в якому зберігаються 1000 слів.
# Створіть словник із ключами - унікальними словами та значеннями - кількістю повторів кожного слова у послідовності.
import random
import urllib.request
import urllib

word_sourse = "https://www.mit.edu/~ecprice/wordlist.10000"
rqst = urllib.request.urlopen(word_sourse).read().decode()
list_of_words = rqst.splitlines()

lst = []
dct = {}
cnt = 0

for _ in range(1000):
    lst.append(random.choice(list_of_words))

for key in lst:
    if key in dct.keys():
        cnt += 1
        dct[key] = cnt
    else:
        dct[key] = 1

print(f"This is the required dictionary: {dct}")
