from core.library import Book, Library

library = Library(input("Enter library name: "))

book = Book(
    input("Enter book title: "),
    input("Enter book author: "),
    float(input("Enter book price: ")),
)

library.add_book(book)

print(library)
print(library.books)

