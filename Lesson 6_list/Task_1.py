# Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку,
# а також суму та середнє арифметичне його значень.

lst = []

for x in range(10):
    lst.append(int(input("Please enter the number: ")))

print(f"Max value ={max(lst)}, minimal value is {min(lst)}. An average equals {sum(lst)/len(lst)}.")