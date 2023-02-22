# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення
# списку, додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.

class MyList:
    """Класс списка"""

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None

        if iterable is not None:
            for element in iterable:
                self.add_last(element)

    class _ListNode:
        """Внутренний класс элемента списка"""
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return f'MyList._ListNode({(self.value, id(self.prev), id(self.next))})'

    class _Iterator:
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def empty(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add_first(self, element):
        node = MyList._ListNode(element)

        node.next = self._head
        self._head = node

    def add_before(self, target_node_value, new_node):
        if self._head is None:   # проверка на пустоту первого элемента
            print("The list is empty")
        else:  # цикл перебора элементов
            n = self._head
            while n is not None:
                if n.value == target_node_value:
                    break
                n = n.next  # переход к следующему элементу цикла
            if n is None:  # если закончились все элементы и next == None
                print("Item not in the List")
            else:  # если цикл нашёл n, соответствующий искомому значению
                new_node = MyList._ListNode(new_node)  # создаём новый нод со значением
                new_node.next = n
                if n.prev is not None:  # проверка на то, что n-элемент не первый
                    new_node.prev = n.prev
                    n.prev.next = new_node
                n.prev = new_node

        self._length += 1

    def add_after(self, target_node_value, new_node):
        if self._head is None:  # проверка на пустоту первого элемента
            print("The list is empty")
        else:  # цикл перебора элементов
            n = self._head
            while n is not None:
                if n.value == target_node_value:
                    break
                n = n.next  # переход к следующему элементу цикла
            if n is None:  # если закончились все элементы и next == None
                print("Item not in the List")
            else:  # если цикл нашёл n, соответствующий искомому значению
                new_node = MyList._ListNode(new_node) # создаём новый нод со значением
                new_node.prev = n  # превязываем предыдущее значение нового нода к найденному значению
                new_node.next = n.next  # привязываем следующее значение нового нода к следующему значению найденного
                if n.next is not None:  # если найденное значение не является последним, то
                    n.next.prev = new_node  # присваиваем старому следующему значению новый нод как предыдущее (вместо n)
                n.next = new_node  # присваиваем найденному значению новый нод как следующий

        self._length += 1

    def add_last(self, element):
        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
            node.next = None

        self._length += 1

    def del_any_element(self, element):
        if self._head is None:  # проверка на пустоту первого элемена
            print("The list is empty")
        else:  # цикл перебора элементов
            n = self._head
            while n is not None:
                if n.value == element:
                    break
                n = n.next  # переход к следующему элементу цикла
            if n is None:  # если закончились все элементы и next == None
                print("Item not in the List")
            else:  # если цикл нашёл n, соответствующий искомому значению
                n.value = None
                n.next.prev = n.prev
                n.prev.next = n.next
                n.next = None
                n.prev = None

        self._length -= 1

    def del_last(self):
        if self._tail == self._head:
            print("There are no elements in the list!")
        else:
            self._tail.prev.next = None
            self._tail.value = None

        self._length -= 1


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list)

    print()

    # Обход списка
    for element in my_list:
        print(element)

    print()

    # Повторный обход списка
    for element in my_list:
        print(element)

    print()

    print("Adding 0 at the beginning:")
    MyList.add_first(my_list, 0)
    print(my_list, '\n')

    print("Adding 6 to the end:")
    MyList.add_last(my_list, 6)
    print(my_list, '\n')

    print("Adding 3 after 5:")
    MyList.add_after(my_list, 5, 3)
    print(my_list, '\n')

    print("Adding 4 before 5:")
    MyList.add_before(my_list, 5, 4)
    print(my_list, '\n')

    print("Adding 4 before 7 (7 not in the list):")
    MyList.add_before(my_list, 7, 4)  # returns "Item not in the List"
    print(my_list, '\n')

    print("Deleting the chosen element:")
    MyList.del_any_element(my_list, 4)
    print(my_list, '\n')

    print("Deleting the last element:")
    MyList.del_last(my_list)
    print(my_list, '\n')

    print("Emptying the list:")
    MyList.empty(my_list)
    print(my_list, '\n')

    print("Deleting last element of empty list:")
    MyList.del_last(my_list)  # There are no elements in the list!
    print(my_list, '\n')


if __name__ == '__main__':
    main()
