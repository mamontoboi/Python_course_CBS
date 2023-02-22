# Створення кортежів
my_tuple = ()
print(my_tuple)

my_tuple1 = (1,)
print(my_tuple1)

my_tuple2 = 1,
print(my_tuple2)

my_tuple3 = (1, 2, 'a string')
print(my_tuple3)

my_tuple4 = 1, 2, 'a string'
print(my_tuple4)

my_tuple5 = tuple(range(8))
print(my_tuple5)
# Кількість двійок у кортежі my_tuple5
print("Number of 2 in the tuple: ", my_tuple5.count(2))
my_tuple6 = (3, 2, 2, 3, 1, 2, 4, 3, 2, 2.0)
print(my_tuple6)
# Кількість двійок у кортежі my_tuple6
print(my_tuple6.count(2))
# отримання індексу (позиції) елемента у кортежі
print('Індекс =', my_tuple6.index(3))
# Rcvs value in 2nd position
print('Psn: ', my_tuple6[2])
# отримання індексу (позиції) неіснуючого елемента у кортежі - ValueError
# print('Індекс =', my_tuple6.index(5))
print(my_tuple6.index(1, 2))  # returns first 1 searching from 2nd element
print(my_tuple6.index(2, 4, 6))  # returns first 2 searching from 4th element to 6th (not including 6th element)
