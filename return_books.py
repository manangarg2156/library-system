from books import books, issued_books
def return_books():
  name = input("Enter the books name: ")
  if name in issued_books:
    issued_books.remove(name)
    books.append(name)
    print("Book Returned")
  else:
    print("There is no books to return")