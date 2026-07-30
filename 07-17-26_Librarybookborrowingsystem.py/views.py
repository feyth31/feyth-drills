from models import books


def show_all_books():
    print("\n=== ALL BOOKS ===")
    for i, book in enumerate(books, start=1):
        status = "Borrowed" if book["is_borrowed"] else "Available"

        print(f"\n{i}. {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {status}")

        if book["is_borrowed"]:
            print(f"Borrowed By: {book['borrowed_by']}")


def borrow_book():
    show_all_books()

    choice = int(input("\nEnter book number to borrow: "))

    if 1 <= choice <= len(books):
        book = books[choice - 1]

        if book["is_borrowed"]:
            print("Book is already borrowed.")
        else:
            student = input("Enter student name: ")
            book["is_borrowed"] = True
            book["borrowed_by"] = student
            print("Book borrowed successfully.")
    else:
        print("Invalid book number.")


def return_book():
    show_all_books()

    choice = int(input("\nEnter book number to return: "))

    if 1 <= choice <= len(books):
        book = books[choice - 1]

        if book["is_borrowed"]:
            book["is_borrowed"] = False
            book["borrowed_by"] = ""
            print("Book returned successfully.")
        else:
            print("Book is already available.")
    else:
        print("Invalid book number.")


def show_available_books():
    print("\n=== AVAILABLE BOOKS ===")

    for book in books:
        if not book["is_borrowed"]:
            print(f"{book['title']} by {book['author']}")


def show_borrowed_books():
    print("\n=== BORROWED BOOKS ===")

    found = False

    for book in books:
        if book["is_borrowed"]:
            found = True
            print(f"{book['title']} - Borrowed by {book['borrowed_by']}")

    if not found:
        print("No borrowed books.")


while True:

    print("\n===== LIBRARY BOOK BORROWING SYSTEM =====")
    print("1. Show All Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Show Available Books")
    print("5. Show Borrowed Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        show_available_books()
    elif choice == "5":
        show_borrowed_books()
    elif choice == "6":
        print("Thank you for using the Library Book Borrowing System!")
        break
    else:
        print("Invalid choice. Please try again.")