# Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.

def nat_fig_sum(a, b):
    """
    Calculates the sum of numbers in a given range.
    """
    if b == a:
        return b
    return b + nat_fig_sum(a, b - 1)


num_1, num_2 = int(input("Please write the starting number: ")), int(input("Please write the ending number: "))
print(f"The sum of all natural numbers in given range is: {nat_fig_sum(num_1, num_2)}")
