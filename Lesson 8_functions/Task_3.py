# Створіть програму-калькулятор, яка підтримує наступні операції:
# додавання, віднімання, множення, ділення, зведення в ступінь, зведення до квадратного та кубічного коренів.
# Всі дані повинні вводитися в циклі, доки користувач не вкаже, що хоче завершити виконання програми.
# Кожна операція має бути реалізована у вигляді окремої функції.
# Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.

import math


def data_for_one():
    return int(input("Enter a = "))


def data_for_two():
    return int(input("Enter a = ")), int(input("Enter b = "))


def total(nums):
    summa = 0
    for num in nums:
        summa += num
    return summa


def sqr_root():
    a = data_for_one()
    return math.sqrt(a)


def cube_root():
    a = data_for_one()
    return math.cbrt(a)


def substr():
    a, b = data_for_two()
    return a - b


def division():
    a, b = data_for_two()
    if not b:
        return "You cannot divide by 0"
    else:
        return a / b


def mult():
    a, b = data_for_two()
    return a * b


def sinus():
    angle_rad = (data_for_one())*math.pi/180
    return round(math.sin(angle_rad), 4)


def cosinus():
    angle_rad = (data_for_one())*math.pi/180
    return round(math.cos(angle_rad), 4)

def pow():
    a, b = data_for_two()
    return a ** b


while True:
    choice_1 = input('''Choose an action: 
    
    +    -    /    *  
    sin    cos   pow 
    sqr_root cube_root 
    
Or write "stop" to end the programme.
''').lower()

    match choice_1:
        case '+':
            num_lst = []
            x = int(input("Number or 0 to finish: "))
            while x != 0:
                num_lst.append(x)
                x = int(input("Number or 0 to finish: "))
            print(total(num_lst))
            continue
        case '-':
            print(substr())
            continue
        case '/':
            print(division())
            continue
        case '*':
            print(mult())
            continue
        case 'sin':
            print(sinus())
            continue
        case 'cos':
            print(cosinus())
            continue
        case 'sqr_root':
            print(sqr_root())
        case 'cube_root':
            print(cube_root())
        case 'pow':
            print(pow())
        case "stop":
            break
        case _:
            print("Wrong entry! Try again")
            continue
print("The programme is completed.")