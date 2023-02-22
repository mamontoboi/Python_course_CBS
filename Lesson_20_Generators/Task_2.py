# Виведіть із списку чисел список квадратів парних чисел. Використовуйте 2 варіанти рішення: генератор та цикл

def generator(nums):
    for x in nums:
        if x % 2 == 0:
            yield x ** 2


lst = [1, 3, 7, 9, 8, 20, 33, 35, 25, 44, 89, 61, 13, 0, 11, 4, 48, 62]

new_lst = []
for i in lst:
    if i % 2 == 0:
        new_lst.append(i ** 2)
print(new_lst)

print(list(generator(lst)))

print(list((j ** 2) for j in lst if j % 2 == 0))
