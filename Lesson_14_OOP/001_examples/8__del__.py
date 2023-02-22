class MyClass:
    """__del__(self) – деструктор об'єкта. Він визначає поведінку об'єкта в той час, коли об'єкт потрапляє до збирача
    сміття; __del__ завжди викликається після завершення роботи інтерпретатора"""

    """Any changes made to __del__ method just add functionality to the inbuilt method. He can smoothly manage his job 
    without any extra help from your side.
    """
    def __del__(self):
        print('___deleting an object___')


mc = MyClass()
