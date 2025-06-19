class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")

# Example
lib = Library()
lib.add_book(Book("Python Basics", "John"))
lib.add_book(Book("OOP Concepts", "Alice"))
lib.show_books()
