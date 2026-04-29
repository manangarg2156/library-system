from books import books
def show_books():
  if len(books)==0:
    print("No Books Available")
  else:
    print("Books Available")
    for b in books:
      print(b)
