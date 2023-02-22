# 1. Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

# 2. Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Book:
    def __init__(self, author, title, year, genre, reviews=None):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):  # to fill the list with reviews
        self.reviews.append(review)

    def __str__(self):
        return f"The {self.author}, {self.title} by  was written in {self.year}. It is {self.genre}. " \
               f"The review are the following: \n{self.reviews}"

    def __repr__(self):
        return f"{self.author}, {self.title}, {self.year}, {self.genre}, {self.reviews}"

    def print_book(self):  # to print book title with corresponding reviews
        print(self.title, self.reviews)


orwell = Book('George Orwell', '1984', '1949', 'dystopian novel')
huxley = Book('Aldous Huxley', 'Brave New World', '1932', 'dystopian novel')
eco = Book('Umberto Eco', 'Foucault\'s Pendulum', '1988', 'satirical novel')

print(orwell.__repr__())
print(orwell)  # 'print' receives format from __str__ method, if __str__ has been detailed in class description
print(huxley.title)
print(eco.genre)

eco.add_review('The satirical novel is full of esoteric references to Kabbalah, alchemy, and conspiracy theory')
eco.add_review('Historical detective-philosophical parody novel')

eco.print_book()
