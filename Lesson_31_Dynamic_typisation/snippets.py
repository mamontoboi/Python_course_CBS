import os

def list_of_files():
    # def list_of_files(self) -> List[File()]:
    lst = []
    for file in os.listdir():
        # file = File(file)
        lst.append(file)
    print(f'List of the files: \n{lst}')
    return lst


# def list_of_subdirs(self) -> 'Type[Directory()]':
def list_of_subdirs():
    lst = []
    for file in os.listdir():
        if os.path.isdir(file):
            # file = Directory(str(file))
            lst.append(file)
    # print(f'List of the subdirectories: \n{lst}')
    return lst

list_of_subdirs()
list_of_files()