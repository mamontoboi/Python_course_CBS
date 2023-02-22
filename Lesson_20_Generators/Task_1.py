# Напишіть генератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).

def gen_rev(nums):
    for i in range(len(nums)):
        yield nums[(len(nums) - i - 1)]


lst = [1, 3, 7, 9, 8, 20, 33, 35]

print(list(gen_rev(lst)))

print(list(lst[-i - 1] for i in range(len(lst))))
