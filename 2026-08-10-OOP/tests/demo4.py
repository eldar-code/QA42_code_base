from core.library import Library, Book

lib = Library(input("Enter library name: "))

add_more_books = True

while add_more_books:
    lib.add_book(Book(
        input("Enter book title: "),
        input("Enter book author: "),
        float(input("Enter book price: ")),
    ))
    if input("Do you want to add anther book? Y/N: ") != "Y":
        add_more_books = False

print("-" * 60)
print(lib)
print(f"Number of books: {len(lib.books)}")
for book in lib.books:
    print(book)
