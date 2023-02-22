# Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3 символи кожного слова.

import re


def last_three(sentence):
    result = re.findall(r'\w*(\w{3})', sentence)
    print(result)


last_three(input("Write your sentence: \n"))
