from books import books, issued_books
from show_books import show_books

def issue_books():
    show_books()
    name = input("Enter the books name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book issued")
    else:
        print("There is no books to issue")