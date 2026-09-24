class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False


class Patron:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register(self, patron):
        self.patrons.append(patron)

    def borrow(self, book, patron):
        if not book.borrowed:
            book.borrowed = True
            patron.books.append(book)
            print(patron.name, "borrowed", book.title)

    def return_book(self, book, patron):
        if book in patron.books:
            book.borrowed = False
            patron.books.remove(book)
            print(patron.name, "returned", book.title)


# Example
library = Library()

book = Book("Python Basics")
patron = Patron("Alice")

library.add_book(book)
library.register(patron)

library.borrow(book, patron)
library.return_book(book, patron)
