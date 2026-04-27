# Input and Output
# Learn how to interact with users through input() and print()

"""
Python Core - 01 Basics
File: 02_input_output.py
Description: Handling user input, printing outputs, and type casting.
"""

# 1. Basic Input and Output
# The input() function pauses execution and waits for the user to type something.
# It ALWAYS returns a string (str).
print("--- Basic I/O ---")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 2. String Formatting (f-strings)
# Introduced in Python 3.6, f-strings (format strings) are the most modern and 
# readable way to inject variables into text. Just put an 'f' before the quotes.
print("\n--- f-strings ---")
full_name = f"{first_name} {last_name}"
print(f"Welcome to Python, {full_name}!")

# 3. Type Casting (Converting data types)
# Because input() always returns a string, we must convert it if we want to do math.
print("\n--- Type Casting ---")

# We wrap the input() function inside int() or float() to convert it immediately.
birth_year = int(input("Enter your birth year (e.g., 2000): "))
current_year = 2026

# Now we can safely subtract them because both are integers.
estimated_age = current_year - birth_year

print(f"You are turning {estimated_age} years old this year.")

# 4. Multiple arguments in print()
# You can pass multiple comma-separated values to print(), and it will automatically 
# add a space between them.
print("\n--- Print Options ---")
print("Data saved:", first_name, birth_year, "- Status: Active")