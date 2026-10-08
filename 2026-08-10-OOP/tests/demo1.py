from core.library import Book, Library

# create a libray instance
adults_libray = Library("Adults")

# create books and add to the library
adults_libray.add_book(Book("AAA", "Fabian", 150))
adults_libray.add_book(Book("BBB", "Eldar", 85))
adults_libray.add_book(Book("CCC", "Ilia", 300))

# print the library
print(adults_libray)

# print all books
for book in adults_libray.books:
    print(book)
print("=" * 60)
# create a libray instance
kids_libray = Library("Kids")

# create books and add to the library
kids_libray.add_book(Book("DDD", "Fabian", 150))
kids_libray.add_book(Book("EEE", "Eldar", 85))
kids_libray.add_book(Book("FFF", "Ron", 300))
kids_libray.add_book(Book("GGG", "Hadeel", 250))
kids_libray.add_book(Book("HHH", "Almog", 270))

# print the library
print(kids_libray)

# print all books
for book in kids_libray.books:
    print(book)
