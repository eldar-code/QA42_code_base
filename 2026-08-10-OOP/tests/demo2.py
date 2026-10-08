from core.library import Library, Book

library = Library(input("Enter library name: "))
print(library)

title = input("Enter book title: ")
author =  input("Enter book author: ")
price = float( input("Enter book price: "))
book = Book(title, author, price)

library.add_book(book)

print(f"{library}. books: {library.books}")

