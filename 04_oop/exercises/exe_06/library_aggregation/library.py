from book import Book

class Library:

    def __init__(self, name: str):
        self.name = name
        self.catalog = []

    def add_book(self, book: Book):
        self.catalog.append(book)
    
    def show_books(self):
        print(f"\n--- Books on the library {self.name} ---\n")
        for book in self.catalog:
            print(f"{book.get_details()}")
