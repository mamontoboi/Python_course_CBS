with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")


# Open file for reading in Binary mode
with open(r'some.txt', "r+b") as fp:
    # Move the file handle to the 5th character from the beginning of the file
    fp.seek(5)
    # read 5 bytes and convert it to string
    print(fp.read(5).decode("utf-8"))

    # Move the fp 10 points ahead from current position read 5 bytes and convert it to string
    fp.seek(10, 1)
    # again read 6 bytes
    print(fp.read(6).decode("utf-8"))
    fp.seek(0, 2)
    fp.write("\nKipling, If".encode('utf-8'))