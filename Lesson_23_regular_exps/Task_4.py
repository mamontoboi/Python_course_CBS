# Напишіть функцію, яка буде аналізувати текст, що надходить до неї, і виводити тільки унікальні слова на екран, загальну
# кількість слів і кількість унікальних слів.

import re


def text_uniqueness_identifier(text):
    text_split = re.split(r'\W', text.lower())
    length_of_text = len(text_split)
    set_of_words = set(text_split)
    quant_set_of_words = len(set_of_words)
    return f'To make the whole phrase of {length_of_text} words only {quant_set_of_words} words were used. ' \
           f'Those are the following:\n{set_of_words}'


print(text_uniqueness_identifier(input("Write your phrase here: \n")))
