string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Ітерування
for character in string:
    print(character)

# Отримання доступу до елементів за допомогою цілих ключів (індексація)
print(string[0])  # L
print(string[2])  # r
print(string[-1])  # .

print(string[15::5])  # ottneasgt - from 15 with step 5. 15th, 20th, 25th etc.
print(string[-15::5])   # ice - from -15 with step 5. -15th, -10th, -5th.
print(string[-15::-5])   # iue a dpr - from -15 with step -5. -15th, -20th, -25th.
print(string[15:5])   # nothing. Not valid request. No values in range from 15 to 5 going to right.
print(string[::-1])   # Reverses the string

# Довжина послідовності
print('Length:', len(string))

print('Min element in string:', min(string))  # empty because the min element is space
print('Max element in string:', max(string))  # u. u has the biggest ASCII value

string2 = string.find("a")
print(string.find("a"))  # 22. First use of a in string
print(string.count("a"))   # 2. Two "a" in a string
print('New string is:', ((string + str(string2) + " ") * 3))
