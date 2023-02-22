# Банківський вклад Користувач робить внесок у розмірі a рублів строком на роки під 10% річних
# (кожний рік розмір його вкладу збільшується на 10%.
# Ці гроші додаються до суми вкладу, і на них наступного року теж будуть відсотки).
# Написати функцію bank, що приймає аргументи a та years, і повертає суму, яка буде на рахунку користувача.

def bank(val, month, percent=10):
    """
    The function calculates the final amount on the bank account after completion of the term of the deposit.
    """
    if month == 1:
        return val * (((percent/12) + 100) / 100)
    return bank(val * (((percent/12) + 100) / 100), month - 1, percent)


amnt = int(input("What is the sum of deposit? \n"))
term = float(input("How long will be the deposit, in months? \n"))
rate = float(input("What's gonna be the interest rate, in %? \n"))

print(f'The total amount accumulated during the whole term of '
      f'deposit will be USD {round(bank(amnt, term, rate), 2)}')

print("Good Bye")
