"""
Python Core - 05 Advanced
File: 05_context_managers.py
Description: Understanding Context Managers, file manipulation, and automatic resource cleanup using 'with'.
"""
import os
import json

print("--- 1. The Old Way vs The Pythonic Way (with open) ---")
filename = "sample_test.txt"

# THE OLD WAY (Dangerous): If an error happens before .close(), the file stays locked in memory!
file = open(filename, "w")
file.write("Hello, this is the old way of writing files.\n")
file.close()

# THE PYTHONIC WAY (Context Manager): The 'with' block automatically closes the file when execution leaves indentation.
with open(filename, "w") as file:
    file.write("Hello, this is the Pythonic way using a Context Manager!\n")
    file.write("Even if the code crashes inside this block, the file WILL be safely closed.\n")

print(f"File '{filename}' created and safely closed without manual syntax.\n")


print("--- 2. File Modes: Reading (r), Writing (w), and Appending (a) ---")
# Mode 'w' (Write): OVERWRITES the file completely.
# Mode 'a' (Append): Adds content to the END of the file without erasing existing data.
# Mode 'r' (Read): Reads the file content (Default mode).

with open(filename, "a") as file:
    file.write("This line was APPENDED to the end of the file.\n")

print("Reading the full content of the file:")
with open(filename, "r") as file:
    content = file.read()
    print(content)


print("--- 3. Working with JSON Files (The Industry Standard) ---")
# In real-world applications, we rarely store data in plain text. We use JSON (JavaScript Object Notation),
# which converts directly to Python Dictionaries and Lists!

user_profile = {
    "username": "Isaque",
    "role": "Admin",
    "modules_completed": ["OOP", "Advanced"],
    "is_active": True
}

json_filename = "user_data.json"

# Saving a Python Dictionary to a JSON file using json.dump()
with open(json_filename, "w") as json_file:
    json.dump(user_profile, json_file, indent=4)
print(f"Dictionary successfully saved to '{json_filename}'.")

# Loading a JSON file back into a Python Dictionary using json.load()
with open(json_filename, "r") as json_file:
    loaded_data = json.load(json_file)

print(f"Data loaded from JSON! Username: {loaded_data['username']}, Role: {loaded_data['role']}\n")


print("--- 4. Creating Your Own Context Manager (The Behind-the-Scenes) ---")
# A custom context manager is just a class that implements __enter__ and __exit__ magic methods!

class CustomDatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"[DB LOG] Connecting to database '{self.db_name}'...")
        return self # This becomes the variable after 'as'

    def query(self, sql):
        print(f"[DB LOG] Executing SQL: {sql}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val, exc_tb capture any error that happened inside the 'with' block
        print(f"[DB LOG] Closing database connection to '{self.db_name}' safely.\n")
        return False # If True, it would suppress any exception that occurred

with CustomDatabaseConnection("Production_DB") as db:
    db.query("SELECT * FROM users")
    db.query("UPDATE users SET status = 'active'")
# Notice that __exit__ runs automatically right here!


# Cleanup our generated files so we don't leave clutter on your hard drive
os.remove(filename)
os.remove(json_filename)
print("Temporary test files cleaned up!")