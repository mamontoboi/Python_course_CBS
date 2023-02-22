# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list.
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list,
# repeat кількість разів. Очистіть список int_list.

import random

int_list = []
new_list = []
rpt_list = []

len_int_lst = int(input("How many numbers do you want to have in the initial list? "))
len_new_lst = int(input("How many times do you want to repeat the initial list? "))

for _ in range(len_int_lst):
    numb = random.randint(1, 1000)
    int_list.append(numb)

for i in range(len(int_list)):
    if i % 2 != 0:
        new_list.append(int_list[i])

int_list.clear()
rpt_list = new_list * len_new_lst
print(f"The New List is {new_list}, \nAnd New List repeated N-times: {rpt_list}")