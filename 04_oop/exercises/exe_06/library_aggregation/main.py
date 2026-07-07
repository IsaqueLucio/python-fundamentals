"""
Exercise 1: Library Aggregation
Main File: main.py
Dependencies to create in the same folder: book.py, library.py

--- Rules for 'book.py' ---
1. Create a class 'Book'.
2. The __init__ should take 'title' (str) and 'author' (str).
3. Create a method 'get_details(self)' returning the formatted string: "[title] by [author]".

--- Rules for 'library.py' ---
1. Import the 'Book' class.
2. Create a class 'Library'.
3. The __init__ should take 'name' (str). Inside it, initialize an empty list called 'catalog'.
4. Create a method 'add_book(self, book: Book)'. This method should append the received book to the 'catalog' list.
5. Create a method 'show_books(self)'. It should iterate over the 'catalog' list and print the details of each book.

--- Rules for 'main.py' (This file) ---
1. Import both 'Book' and 'Library' classes.
2. Create 3 independent Book objects (e.g., Lord of the Rings, Harry Potter, etc).
3. Create 1 Library object.
4. Add the 3 books to the library using the 'add_book' method (Aggregation).
5. Call the 'show_books()' method on the library.
"""

