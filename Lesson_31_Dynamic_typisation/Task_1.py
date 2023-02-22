# Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень
# вихідного масиву. Додайте анотацію типів для вхідних і вислідних значень функції.

from typing import List
import unittest


def converter(lst: List[int]) -> List[str]:
    out = []
    [out.append(str(item)) for item in lst]
    return out


print(converter([1, 2, 3, 4, 5, 6]))


class UtilsTest(unittest.TestCase):
    def test_converter(self):
        result = converter(converter([1, 2, 3, 4, 5, 6]))
        expected = ['1', '2', '3', '4', '5', '6']
        self.assertEqual(result, expected)
