# Написати функцію, яка за допомогою регулярних виразів розбиває текст на окремі слова і знаходить частоту окремих слів.

import re


def words_counter(string):
    result = re.split(r'[\W]', string.lower())
    word_freq = {}
    for i in result:
        if i == '':
            continue
        elif i in word_freq.keys():
            word_freq[i] += 1
        else:
            word_freq[i] = 1
    sorted_tuple = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    final_dict = {k: v for k, v in sorted_tuple}
    return final_dict


text = "Locate the insertion point for x in a to maintain sorted order." \
       "The parameters lo and hi may be used to specify a subset of the list which should be considered;" \
       "by default the entire list is used. If x is already present in a," \
       "the insertion point will be before any existing entries. The return value is suitable" \
       "for use as the first parameter to list.insert() assuming that a is already sorted."""

print(words_counter(text))
