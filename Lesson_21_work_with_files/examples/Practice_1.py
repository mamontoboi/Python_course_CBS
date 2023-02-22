"""Creating the file and writing the text in it"""

kipling2 = open("../if_2.txt", 'a+', encoding="UTF-8")
kipling2.writelines("If you can dream and not make dreams your master \n"
                    "If you can think and not make thoughts your aim \n"
                    "If you can meet with Triumph and Disaster \n"
                    "And treat those two impostors just the same \n"
                    "If you can bear to hear the truth you ve spoken \n"
                    "Twisted by knaves to make a trap for fools \n"
                    "Or watch the things you gave your life to, broken, \n"
                    "And stoop and build them up with worn-out tools:")
kipling2.close()
"""Closing file for amendment and opening it for reading. Files, opened not with r cannot be read line by line"""
kipling2 = open("../if_2.txt", 'r+')

lst = ""
for line in kipling2:
    lst += kipling2.read() + '\n'  # adding lines from if_2 into the string in order to import them into practice.txt

print(lst)

with open("practice.txt", 'r+') as practice_file:
    for line in practice_file:
        print(line, end='')
    practice_file.seek(0, 2)
    practice_file.write('\nKipling. If')
    practice_file.seek(0, 2)
    practice_file.write('\n')
    # practice_file.writelines(lst)  # writes lines from if_2 into practice
    for line in practice_file:
        x = practice_file.readline()
        print(x, end='')

lst_of_rows = kipling2.readlines()
print(lst_of_rows)

lst_of_rows_lst = list(kipling2)
print(lst_of_rows_lst)

kipling2.close()


