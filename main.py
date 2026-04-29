from books import books, issued_books
from add_books import add_books
from show_books import show_books
from issue_books import issue_books
from return_books import return_books

def main():
  while True:
    print("1. Add Books")
    print("2. Show Books")
    print("3. Issue Books")
    print("4. Return Books")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
      add_books()
    elif choice == 2:
      show_books()
    elif choice == 3:
      issue_books()
    elif choice == 4:
      return_books()
    elif choice == 5:
      break
    else:
      print("Invalid Choice")

main()