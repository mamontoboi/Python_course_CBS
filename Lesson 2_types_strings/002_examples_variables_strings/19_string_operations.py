str1 = 'hel'
str2 = 'lo'
# конкатенація рядків
result = str1 + str2

print(result)

# форматування рядків
a = 48
b = 73

message1 = '%d - %d = %d' % (a, b, a - b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)

message3 = f'{a} - {b} = {a - b}'
print(message3)

# індексація рядків
s = 'Hello, World!'

# індексація починається з нуля
print(s[0])
# четвертий (п'ятий логічно) елемент (символ)
print(s[4])
# негативні числа - індексація з кінця
print(s[-1])

# символи з другого (включно) до сьомого (не включно)
print(s[2:7])
# те саме, але з кроком два
print(s[2:7:2])

print(s[:4:3])  # Hl - from 0 to 4 (not including) with step 3
print(s[-1::-1])  # !dlroW ,olleH  - vise versa
print(s[::-1])  # same

print(s[-1:0:-1])  # !dlroW ,olle   No H as 0th element is not included

print(str1.find('l'))  # returns psn
print(str1.find('o'))  # returns -1 if not found
print(str1.index('o'))  # returns ValueError if not found

