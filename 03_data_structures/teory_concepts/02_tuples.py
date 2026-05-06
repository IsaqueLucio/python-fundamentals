"""
Python Core - 03 Data Structures
File: 02_tuples.py
Description: Creating, accessing, unpacking, and understanding tuple immutability.
"""

print("--- 1. Creation and Access ---")
# Tuples are defined by parentheses () instead of square brackets []
# (Though the parentheses are actually optional, it's best practice to use them)
database_config = ("localhost", 5432, "admin", "super_secret_pass")

# Accessing and Slicing works EXACTLY like lists
print(f"Host: {database_config[0]}")
print(f"Port: {database_config[1]}")
print(f"Credentials: {database_config[2:]}") # Slicing still works!


print("\n--- 2. The Immutable Nature ---")
# If you uncomment the line below, Python will crash with a TypeError
# database_config[1] = 8080  # ERROR: 'tuple' object does not support item assignment

print("Tuples cannot be changed after creation. They are completely read-only.")


print("\n--- 3. Tuple Unpacking (Python Superpower) ---")
# Unpacking allows you to extract tuple values directly into distinct variables in a single line.
# This is heavily used when a function returns multiple values.
server_host, server_port, db_user, db_pass = database_config

print(f"Unpacked variables -> Host: {server_host} | User: {db_user}")


print("\n--- 4. Built-in Methods ---")
# Because tuples can't be modified, they only have 2 built-in methods: count() and index()
status_codes = (200, 404, 200, 500, 200, 403)

# .count() returns how many times a value appears in the tuple
success_count = status_codes.count(200)
print(f"The code 200 appeared {success_count} times.")

# .index() returns the FIRST position where a value is found
error_position = status_codes.index(404)
print(f"The first 404 error was found at index {error_position}.")