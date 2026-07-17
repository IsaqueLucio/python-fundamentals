"""
Exercise 1: The Safe Diary Writer
Main File: main.py

Rules:
1. Import 'os' and create a variable for the secure file path:
   file_path = os.path.join(os.path.dirname(__file__), "diary.txt")
2. Use a 'with open()' block in write mode ("w") to create 'diary.txt' and write two lines of text:
   - "Day 1: Started learning Context Managers.\n"
   - "Day 2: Mastered the 'with' syntax.\n"
3. Use a second 'with open()' block in append mode ("a") to add a third line to the end of the file:
   - "Day 3: Built secure file paths!\n"
4. Use a third 'with open()' block in read mode ("r") to read the entire file content using '.read()'.
5. Print the read content to the terminal to verify all three lines are there!
"""

import os

file_path = os.path.join(os.path.dirname(__file__), "diary.txt")

with open(file_path, "w") as file:
    print(type(file_path))
    file.write("Day 1: Started learning Context Managers.\n")
    file.write("Day 2: Mastered the 'with' syntax.\n")

with open(file_path, "a") as file:
    file.write("Day 3: Built secure file paths!\n")

with open(file_path, "r") as file:
    content = file.read()
    print(content)