# Дано два рядки. Виведіть на екран символи, які є в обох рядках.
import string, random

set_a, set_b = set(), set()

for _ in range(random.randint(1,26)):
    set_a.add(random.choice(string.ascii_lowercase))
    set_b.add(random.choice(string.ascii_lowercase))

common = set_a.intersection(set_b)

print("The list of the common elements is the following:{}".format(common))
