# To make an amendment to the code it is enough to uncommit one of the committed functions and update
# choice as appropriate. Or you may add something of your own.

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


# TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
# def sqr_root():
#     a = data_for_one()
#     return math.sqrt(a)


# TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
# def cube_root():
#     a = data_for_one()
#     return math.cbrt(a)


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


def cosine():
     angle_rad = (data_for_one())*math.pi/180
     return round(math.cos(angle_rad), 4)


# TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
# def power():
#     a, b = data_for_two()
#     return a ** b

def bank(val, month, percent=10):
    """
    The function calculates the final amount on the bank account after completion of the term of the deposit.
    """
    if month == 1:
        return val * (((percent/12) + 100) / 100)
    return bank(val * (((percent/12) + 100) / 100), month - 1, percent)


print("Welcome to the good old calculator programme.\nYou might think that you have seen it before.\n"
      "And... you're definitely right!")

while True:
    choice_1 = input('''
    Choose an action: 
    
    +    -    /    *   sin  cos
    $$ - for deposit calculation 
    
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
             print(cosine())
             continue
        # TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
        # case 'sqr_root':
        #     print(sqr_root())
        #     TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
        # case 'cube_root':
        #     print(cube_root())
        #     TODO: To be uncommitted to make change to programme. choice_1 to be updated as appropriate
        # case 'pow':
        #     print(power())
        case '$$':
            amnt = int(input("What is the sum of deposit? \n"))
            term = float(input("How long will be the term of the deposit, in months? \n"))
            rate = float(input("What's gonna be the yearly interest rate, in %? \n"))

            print(f'The total amount accumulated during the whole term of '
                  f'deposit will be USD {round(bank(amnt, term, rate), 2)}')
        case "stop":
            break
        case _:
            print("Wrong entry! Try again")
            continue

print("The programme is completed. Thank you for choosing The Calculator!")
print("And thank you very much for using GitРги to co-develop this application.")
