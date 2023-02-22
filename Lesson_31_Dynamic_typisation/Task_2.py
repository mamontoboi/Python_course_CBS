# Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
# Клас Directory має мати такі поля:
# ·        назва (name типу str);
# ·        батьківська тека (root типу Directory);
# ·        список файлів (список типу files, який складається з екземплярів File);
# ·        список підтек (список типу sub_directories, який складається з екземплярів Directory).
#
# Клас Directory має мати такі поля:
# ·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root для приймального екземпляра);
# ·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root. Метод також видаляє теку зі списку sub_directories);
# ·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас File нижче);
# ·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory. Метод видаляє файл зі списку files).
#
# Клас File має мати такі поля:
# ·        назва (name типу str);
# ·        тека (Directory типу Directory).

import os
from typing import List, Sequence


class File:
    def __init__(self, name: str):
        self.name = name
        self.direct = self.direct()

    @staticmethod
    def direct():
        return os.getcwd()


class Directory:
    list_of_directories = []

    def __init__(self, name: str):
        self.name = name
        self.list_of_files()
        self.list_of_subdirs()
        self.make_dir(name)
        self.append_list_of_directories(self.name)
        self.root = self.root()

    def root(self):
        # os.chdir(r"..\\")
        root = os.path.dirname(r'..\\.')
        print(root)
        return root

    def list_of_files(self) -> List[File]:
        lst = []
        files = os.listdir()
        for file in files:
            if not os.path.isdir(file):
                file = File(file)
                lst.append(file)
        print(f'List of instances of files in directory:')
        [print(i.name) for i in lst]
        return lst

    def remove_file(self):
        pass

    def list_of_subdirs(self) -> List[str]:
        lst = []
        files = os.listdir()
        for file in files:
            if os.path.isdir(file):
                lst.append(file)
        print(f'List of the subdirectories: \n{lst}')
        return lst

    @classmethod
    def append_list_of_directories(cls, name: str) -> Sequence[str]:
        Directory.list_of_directories.append(name)
        return Directory.list_of_directories

    @classmethod
    def remove_directory_from_list(cls, name: str) -> Sequence[str]:
        Directory.list_of_directories.remove(name)
        return Directory.list_of_directories

    def make_file(self, name: str):
        path = r"{root}\\{name}".format(root=self.root, name=self.name)
        os.chdir(path)
        file = open(name, 'w+')
        file.close()
        file_inst = File(name)
        return file_inst  # type: File

    @classmethod
    def make_dir(cls, name: str, path: str = '.'):
        os.chdir(path)
        os.mkdir(name)


dir = Directory('Hello_you')
print(dir.root)
print(dir.remove_directory_from_list('Hello_you'))

# Directory.make_dir('Direct_1')
# dir.make_file('file_1.txt')
# dir.make_file('file_2.txt')








