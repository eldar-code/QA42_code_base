from core.library import Library, Book

# main object with all application logic
lib = Library("QA42 State Library")


def show_menu():
    print("---------------------------------------")
    print("Add book to library ............ add")
    print("Show all library books ......... all")
    print("Find book by title ............ find")
    print("Find books by author .......... author")
    print("Exit .......................... x")


# functionality comes here ===========
def do_add():
    lib.add_book(Book(
        input("Enter title: "),
        input("Enter author: "),
        float(input("Enter price: ")),
    ))


def do_all():
    print(f"================== List of all books in {lib.name}:")
    for book in lib.books:
        print(book)
    print("=" * 100)


def do_find_by_title():
    title = input("Enter book title: ")
    book = lib.find_book_by_title(title)
    if book:
        print(f"Found: {book}")
    else:
        print(f"Not Found book titled: {title}")

def do_find_by_author():
    author = input("Enter author: ")
    books = lib.find_books_by_author(author)
    print(f"============== Books written by {author}:")
    for book in books:
        print(book)
    print("=========================")


# ======================== ===========

while True:
    show_menu()
    choice = input("Enter your choice: ").lower()

    if choice == "add":
        do_add()
    elif choice == "all":
        do_all()
    elif choice == "find":
        do_find_by_title()
    elif choice == "author":
        do_find_by_author()
    elif choice == "x":
        break
    else:
        print(f"==== The choice {choice} is not supported!!! ====")

print("End of Program!")
