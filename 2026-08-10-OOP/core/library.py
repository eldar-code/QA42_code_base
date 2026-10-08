class Book:
    # class variable - belong to class (not to instances)
    c = 101

    def __init__(self, title: str, author: str, price: float):
        # instance variables (each instance has its own copy)
        self.isbn = Book.c
        self.title = title
        self.author = author
        self.price = price
        # increment the class variable c (the isbn counter)
        Book.c += 1

    def __str__(self) -> str:
        return f"Book[isbn={self.isbn}, title={self.title}, author={self.author}, price={self.price}]"

    def __repr__(self):
        return f"Book[isbn={self.isbn}, title={self.title}, author={self.author}, price={self.price}]"


class Library:

    def __init__(self, name: str):
        self.name = name
        # define that books is a list of Book (all items in the list must be of type Book)
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book_by_title(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_books_by_author(self, author: str) -> list[Book]:
        books: list[Book] = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books

    def __str__(self) -> str:
        return f"Library: {self.name}"
