# Створіть програму, яка приймає як формальні параметри зріст і вагу користувача,
# обчислює індекс маси тіла і в залежності від результату повертає інформаційне повідомлення
# (маса тіла в нормі, недостатня вага або слідкуйте за фігурою).
# Користувач з клавіатури вводить значення росту та маси тіла та передає ці дані у вигляді фактичних параметрів
# під час виклику функції. Програма працює доти, доки користувач не зупинить її комбінацією символів «off».


def bmi(a, b):
    bmi_val = a / b ** 2
    return "Underweight" if bmi_val <= 18.5 else "Normal" if bmi_val <= 25 else "Overweight" if bmi_val <= 30 else "Obese"
    # if bmi_val > 25:
    #     return f'Your BMI value is {round(bmi_val, 1)}. You are too short for your weight. Or maybe too dense.;-)'
    # elif 18.5 <= bmi_val <= 25:
    #     return f'Your BMI value is {round(bmi_val), 1}. You are perfect! Enjoy your body.'
    # elif 0 <= bmi_val < 18.5:
    #     return f'Your BMI value is {round(bmi_val), 1}. You are underweight. Good for you, though, less stress ' \
    #            f'for your joints.'
    # else:
    #     return f'Your BMI value is {round(bmi_val), 1}. Are you an elf?;-) Check the data.'


def main():
    a, b = float(input("What's your weight, in kg? \n")), float(input("What's your height, in mtrs? \n"))
    print(bmi(a, b))
    print()
    choice_1 = input("If you want to finish the programme write 'Off' or press Enter to continue. \n").title()
    while choice_1 != 'Off':
        a, b = float(input("What's your weight, in kg? \n")), float(input("What's your height, in mtrs? \n"))
        print(bmi(a, b))
        print()
        choice_1 = input("If you want to finish the programme write 'Off' \n").title()
        continue


if __name__ == '__main__':
    main()
