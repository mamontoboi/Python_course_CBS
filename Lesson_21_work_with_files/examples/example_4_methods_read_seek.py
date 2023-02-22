"""
Метод seek() - перейти на потрібну нам позицію:

my_file.seek(offset, [from])

Аргумент offset вказує на скільки байт перейти. Опціональний аргумент від означає позицію, з якої починається
рух. 0 означає початок файлу, 1 - нинішня позиція, 2 - кінець файлу.
"""

"""
f.seek(0)	Move file pointer to the beginning of a File
f.seek(5)	Move file pointer five characters ahead from the beginning of a file.
f.seek(0, 2)	Move file pointer to the end of a File
f.seek(5, 1)	Move file pointer five characters ahead from the current position.
f.seek(-5, 1)	Move file pointer five characters behind from the current position.
f.seek(-5, 2)	Move file pointer in the reverse direction. Move it to the 5th character from the end of the file
NOTE: Files, not opened in binary mode, can use offset of seek only from beginning, e.g (10, 0), but not from (10, 1) 
or (-5, 2)"""

my_file = open("some.txt", "r")
print(my_file.read(10))
print("Ми знаходимося на позиції:", my_file.tell())  # Ми знаходимося на позиції: 10
# Повертаємося на початок
my_file.seek(0)
# Читаем снова десять символов
print(my_file.read(10))
# переносимся на 12 позицию от начала. Начало по умолчанию вместо 0 вторым элементом в seek.
my_file.seek(12)
# читаем ещё 30 символов
print(my_file.read(30))
# спрашиваем позицию
print(my_file.tell())  # 43
print()
# read the remaining line
print(my_file.readline())
print(my_file.tell())  # 50
my_file.close()


# Seek in reversed order
# Opening "some.txt" text file in BINARY mode
f = open("some.txt", "rb")  # only binary can be read from the end of the line

# sets Reference point to tenth position to the left from end
f.seek(-10, 2)

# prints current position
print(f.tell())  # 130

# Converting binary to string and printing
print(f.readline().decode('utf-8'))  # man my son

f.close()