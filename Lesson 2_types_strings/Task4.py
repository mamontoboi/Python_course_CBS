phrase = input('Please enter your 10 symbols phrase here: ')
ph_sum = 0

for letter in phrase:
    val = ord(letter)
    ph_sum += val

print(ph_sum)


