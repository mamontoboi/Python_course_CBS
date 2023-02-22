import re

string = 'Test1 Test2 Test3 Test4 Test5'
pattern = "Test"

for i in re.finditer(pattern, string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=i.group(), begin=i.start(),
        end=i.end())
    # Виводимо кожен знайдений результат:
    print(s)
