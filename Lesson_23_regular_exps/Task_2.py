# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження, телефон та електронну
# адресу. Дані потрібно записати до іншого файлу.

import re


def parse_file(initial_file_name, final_file_name):
    with open(initial_file_name, 'r') as in_file:
        for line in in_file:
            dob = ''.join(re.findall(r'(\d{2}-\d{2}-\d{4})', line))
            phone = ''.join(re.findall(r'\+\d+', line))
            email = ''.join(re.findall(r'\w+@\w+\.\w{,3}', line))
            contact_details = f'Date of birth is {dob}, phone is {phone} and mail is {email}. \n'
            print(contact_details)
            try:
                final_file = open(final_file_name, 'x')
            except FileExistsError:
                final_file = open(final_file_name, 'a')
            final_file.writelines(contact_details)
            final_file.close()


parse_file('names_for_test.txt', 'new_names_file.txt')