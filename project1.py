class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.borrowed_by = None

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nBook ID: {self.book_id}\nBorrowed By: {self.borrowed_by}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, book_id):
        book = Book(title, author, book_id)
        self.books[book_id] = book
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book_id, book in self.books.items():
                print(f"Book ID: {book_id} | Title: {book.title} | Author: {book.author}")

    def borrow_book(self, book_id, user_name):
        if book_id in self.books:
            book = self.books[book_id]
            if book.borrowed_by:
                print("Sorry, the book is already borrowed.")
            else:
                book.borrowed_by = user_name
                print(f"Book '{book.title}' is now borrowed by {user_name}.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.borrowed_by:
                print(f"Book '{book.title}' has been returned.")
                book.borrowed_by = None
            else:
                print("The book was not borrowed.")
        else:
            print("Book not found.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book_id = input("Enter book ID: ")
            library.add_book(title, author, book_id)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            book_id = input("Enter book ID to borrow: ")
            user_name = input("Enter your name: ")
            library.borrow_book(book_id, user_name)
        elif choice == "4":
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)
        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
