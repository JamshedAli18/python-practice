# Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added.")

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"You returned '{title}'.")
                return
        print(f"Book '{title}' was not borrowed.")

# User class
class User:
    def __init__(self, name):
        self.name = name

    def borrow(self, library, title):
        library.borrow_book(title)

    def return_book(self, library, title):
        library.return_book(title)

# --- Run Example ---
lib = Library()
lib.add_book("Python Basics", "John Doe")
lib.add_book("OOP Concepts", "Jane Smith")

lib.show_books()

user = User("Jamshed")
user.borrow(lib, "Python Basics")
lib.show_books()

user.return_book(lib, "Python Basics")
lib.show_books()
