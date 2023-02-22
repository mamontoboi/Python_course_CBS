# Для цього завдання вихідний список значень беремо з підсумкового списку new_list додаткового завдання 2.
# Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів та
# його позицію у цьому списку.
import Task_5
from Task_5 import new_list

numb = int(input("Please state the required number: "))
rslt = Task_5.new_list.count(numb)
if rslt > 0:
    psn = Task_5.new_list.index(numb)
    print(f"\n\tThe number {numb} is mentioned in the list {rslt} times."
          f"\n\tIt appears for the first time in the position {psn}")
elif rslt == 0:
    print(f"The number {numb} not in the list.")


