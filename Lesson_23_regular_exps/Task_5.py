# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження,
# електронну адресу та відгук про курси учня. Написати функцію, яка, використовуючи регулярні вирази, витягне дані
# з рядка і поверне словник.

import re


def text_analyser(text):
    dictionary = {}
    dictionary['first_name'] = ''.join(re.findall(r'([A-Z][a-z]+)\s[A-Z][a-z]+', text))
    dictionary['last_name'] = ''.join(re.findall(r'[A-Z][a-z]+\s([A-Z][a-z]+)', text))
    dictionary['DOB'] = ''.join(re.findall(r'(\d{2}-\d{2}-\d{4})', text))
    dictionary['email'] = ''.join(re.findall(r'\w+@\S+\.\S+', text))
    dictionary['Review'] = ''.join(re.findall(r'review: (.*[.!?])', text))
    return dictionary


print(text_analyser("Jesus Christ was born approximately on 25-12-0004 b.c. He didn't have an email, "
                    "although it might sound like god@man.com."
                    "When he was a child he had received the following review: "
                    "Weird little fellow. A bit naive. Most probably he'll die young."))

print(text_analyser(input("Write your text here: \n")))
