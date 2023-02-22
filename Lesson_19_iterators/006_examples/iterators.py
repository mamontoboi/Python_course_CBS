## Counting / counter
# import itertools #in-build module
# counter = itertools.count()
# print(next(counter)) # 0
# print(next(counter)) # 1
# print(next(counter)) # 2

## Example of counting
# import itertools #in-build module
# counter = itertools.count()
# data = [100, 200, 300, 400] # example list
# daily_data = list(zip(itertools.count(), data)) #creates a list of pairs number - data)
# print(daily_data) #[(0, 100), (1, 200), (2, 300), (3, 400)]

## Example of settings of counter
# import itertools #in-build module
# counter = itertools.count(start = 5, step = 5)
# print(next(counter)) #5
# print(next(counter)) #10
# print(next(counter)) #15

## Example of settings of counter
# counter = itertools.count(start = 20, step = 5)
#
# for i in range(5):
#     print(next(counter))
# 20
# 25
# 30
# 35
# 40

## Example of settings of counter with negative step
# import itertools #in-build module
# counter = itertools.count(start = 5, step = -2.5)
# print(next(counter)) #5
# print(next(counter)) #2.5
# print(next(counter)) #0.0
# print(next(counter)) #-2.5

## Example of counting through the longest list
# import itertools #in-build module
# counter = itertools.count()
# data = [100, 200, 300, 400] # example list
# daily_data = list(itertools.zip_longest(range(10), data)) #itertools.zip_longest - to go through the longest list
# print(daily_data) #[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]

## Cycle function
# import itertools #in-build module
# counter = itertools.cycle([1,2,3]) #cycle makes to loop through the list over and over again
# print(next(counter)) #1
# print(next(counter)) #2
# print(next(counter)) #3
# print(next(counter)) #1
# print(next(counter)) #2
# print(next(counter)) #3

## Cycle function with string
# import itertools #in-build module
# counter = itertools.cycle(('ON', 'OFF')) #cycle of switch, that goes on and off
# print(next(counter)) #ON
# print(next(counter)) #OFF
# print(next(counter)) #ON
# print(next(counter)) #OFF
# print(next(counter)) #ON
# print(next(counter)) #OFF

## Repeat function
# import itertools #in-build module
# counter = itertools.repeat(2) #repeat the value indefenately
# print(next(counter)) #2
# print(next(counter)) #2
# print(next(counter)) #2

## Repeat function limited number of times:
# import itertools #in-build module
# counter = itertools.repeat(2, times=2) #repeat the value 2 times, then gives traceback
# print(next(counter)) #2
# print(next(counter)) #2
# print(next(counter)) #StopIteration

## Repeat in order to pass list of constant value to math func:
# import itertools #in-build module
# counter = itertools.repeat(2, times=3) #repeat the value 3 times, then gives traceback
# squares = map(pow, range(10), itertools.repeat(2)) #map loops through all values within range into power of repeat value. 1**2, 2**2,3**2, 4**2 etc
# print(list(squares)) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

## starmap, takes arguments from tuples:
# import itertools #in-build module
# counter = itertools.repeat(2, times=3) #repeat the value 3 times, then gives traceback
# squares = itertools.starmap(pow,[(0,2), (1, 2), (2, 2)]) #map loops through all tuples from argument. 1**2, 2**2, 3**2
# print(list(squares)) #[0, 1, 4]

## Creating all combinations (order doesn't matter in combitations):
# import itertools
# letters = ['a', 'b', 'c', 'd']
# result = itertools.combinations(letters, 2) #creates list of all 2-letters combinations from the list (a,c) or (c,a), not both
# for item in result:
#     print(item)
## ('a', 'b')
## ('a', 'c')
## ('a', 'd')
## ('b', 'c')
## ('b', 'd')
## ('c', 'd')

## Created all combinations when order does matter
# import itertools
# letters = ['a', 'b', 'c', 'd']
# result = itertools.permutations(letters, 2) #creates list of all 2-letters combinations (a,c) and (c,a) both, as order does matter
# for item in result:
#     print(item)
## ('a', 'b')
## ('a', 'c')
## ('a', 'd')
## ('b', 'a')
## ('b', 'c')
## ('b', 'd')
## ('c', 'a')
## ('c', 'b')
## ('c', 'd')
## ('d', 'a')
## ('d', 'b')
## ('d', 'c')

## If we want to create combinations with repeating values, e.g. (a, a), (b, b)
# import itertools
# numbers = [0,1,2,3]
# result = itertools.combinations_with_replacement(numbers, 4) #to creater combinations with repeating values
# for item in result:
#     print(item) #there are a long list of combitation, example below:
## (0, 0, 0, 0)
## (0, 0, 0, 1)
## (0, 0, 0, 2)
## (0, 0, 1, 1)
## (0, 0, 1, 2) etc.

## If we want to create combinations with repeating values - second option, e.g. (a, a), (b, b)
# import itertools
# numbers = [0,1,2,3]
# result = itertools.product(numbers, repeat=4) #to create combinations with repeating values
# for item in result:
#     print(item)
## (0, 0, 0, 0)
## (0, 0, 0, 1)
## (0, 0, 0, 2)
## (0, 0, 0, 3)
## (0, 0, 1, 0)
## (0, 0, 1, 1)
## (0, 0, 1, 2)
## (0, 0, 1, 3)

# import itertools
# numbs = [1, 2, 3, 4]
# counts = ['a', 'b', 'c', 'd']
# result = itertools.product(numbs, counts)
# for i in result:
#     print(*i)
#
# # 1 a
# # 1 b
# # 1 c
# # 1 d
# # 2 a
# # 2 b

## Combining two lists
# import itertools
# numbers = [0,1,2,3]
# letters = ['a', 'b', 'c', 'd']
# names = ['Corey', 'Nicole']
#
# combined = itertools.chain(letters, numbers, names) #chain loop through all mentioned lists
#
# for item in combined:
#     print(item)
## a
## b
## c
## d
## 0
## 1
## 2
## 3
## Corey
## Nicole

## Slicing of the iterator
# import itertools
#
# result = itertools.islice(range(10), 5) #slices first 5 items of the iterable range
# for item in result:
#     print(item)
## 0
## 1
## 2
## 3
## 4

## Slicing of the iterator from start to stop
# import itertools
# result = itertools.islice(range(10), 1, 5) #slices from starting point 1 to stopping point 5
# for item in result:
#     print(item)
## 1
## 2
## 3
## 4


## Slicing of the iterator from start to stop with step
# import itertools
# result = itertools.islice(range(10), 1, 5, 2) #slices from starting point 1 to stopping point 5 with step 2
# for item in result:
#     print(item)
## 1
## 3

## In order to slice several lines from file:
# import itertools
# with open('name of the file', 'r') as f:
#     header = itertools.islice(f, 3) #to slice first 3 rows of the file
#     for line in header:
#         print(line, end='') #prints first 3 rows

## In order to accummulate all values:
# import itertools
#
# numbers = [0,1,2,3,2,1,0]
#
# result = itertools.accumulate(numbers) #accummulates value of numbers: 0+1 = 1+2 = 3+3 = 6+2 = 8+1 = 9+0 = 9
# for item in result:
#     print(item)
## 0
## 1
## 3
## 6
## 8
## 9
## 9

## In order to accummulate-multiply all values:
# import itertools
# import operator
#
# numbers = [1,2,3,2,1]
#
# result = itertools.accumulate(numbers, operator.mul) #multiply value of numbers: 1*2 = 2*3 = 6*2 = 12*1 = 12
# for item in result:
#     print(item)
## 1
## 2
## 6
## 12
## 12