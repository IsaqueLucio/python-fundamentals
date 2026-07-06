"""
Exercise 1: Simple Book Class
File: 02_book_class.py

Rules:
1. Create a class called 'Book'.
2. Create the __init__ method taking 'title' (str) and 'author' (str).
3. Inside __init__, save 'title' and 'author' as instance attributes (using self).
4. Also inside __init__, create an attribute called 'is_read' and set it to False by default.
5. Create a method called 'read_book(self)'. When called, it should change 'self.is_read' to True and print: "You have finished reading [title]".
6. Outside the class, create two Book objects (e.g., book1 and book2).
7. Call the 'read_book()' method on ONLY ONE of the books.
8. Print the 'is_read' attribute for both books to verify that only one is True.
"""

class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_read = False
    
    def read_book(self):
        self.is_read = True
        print(f"You have finished reading {self.title}.")
    
book001 = Book("Harry Potter", "J.K Rowling")
book002 = Book("The Witcher", "Andrzej Sapkowski")

book002.read_book()

print(book001.is_read)
print(book002.is_read)