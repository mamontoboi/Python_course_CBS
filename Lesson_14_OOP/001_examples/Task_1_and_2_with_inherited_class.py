# 1. Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

# 2. Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"The {self.title} by {self.author} was written in {self.year}. It is {self.genre}."

    def __repr__(self):
        return f"{self.author}, {self.title}, {self.year}, {self.genre}"


class Review(Book):
    # inheritance from class Book
    def __init__(self, author, title, year, genre, reviews=None):
        super().__init__(author, title, year, genre)
        self.reviews = []

    def add_review(self, review):  # to fill the list with reviews
        self.reviews.append(review)

    def __repr__(self):
        return f"{self.author}, {self.title}, {self.year}, {self.genre}, {self.reviews}"

    def __str__(self):
        return f"Those are the reviews for the {self.title}: \n{self.reviews}"

    def print_book(self):  # to print book title with corresponding reviews
        print(self.title, self.reviews)


orwell = Book('George Orwell', '1984', '1949', 'dystopian novel')
huxley = Book('Aldous Huxley', 'Brave New World', '1932', 'dystopian novel')
eco = Review('Umberto Eco', 'Foucault\'s Pendulum', '1988', 'satirical novel')

eco.add_review('The satirical novel is full of esoteric references to Kabbalah, alchemy, and conspiracy theory')
eco.add_review('Historical detective-philosophical parody novel')

print(orwell.__str__())
print(repr(orwell))
print(huxley.title)
print(eco.genre)
eco.print_book()
