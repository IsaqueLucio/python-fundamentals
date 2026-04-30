"""
Python Core - 02 Functions
File: 03_lambda_functions.py
Description: Anonymous functions, map(), filter(), and practical use cases.
"""

# 1. Basic Lambda Function
# A lambda function is a small anonymous function.
# It can take any number of arguments, but can only have ONE expression.
# Syntax: lambda arguments: expression (No 'return' keyword needed)
print("--- Basic Lambda ---")

# Regular function
def double_normal(x):
    return x * 2

# Lambda equivalent
double_lambda = lambda x: x * 2

print(f"Normal function: {double_normal(5)}")
print(f"Lambda function: {double_lambda(5)}")

# 2. Multiple Arguments
print("\n--- Multiple Arguments ---")
multiply = lambda a, b: a * b
print(f"5 * 4 = {multiply(5, 4)}")

# 3. Using Lambda for Sorting (Very Common Use Case)
# Lambdas are often used as the 'key' argument in sorting functions
# to tell Python exactly HOW to sort complex data structures like dictionaries.
print("\n--- Sorting with Lambda ---")
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort the list of dictionaries by the 'age' key
# The lambda says: "Look at each user, and use their 'age' value to sort them."
users.sort(key=lambda user: user["age"])

print("Users sorted by age:")
for user in users:
    print(f" - {user['name']} ({user['age']} years old)")

# 4. Using Lambda with map() and filter()
# These functions apply a lambda to every item in an iterable (like a list).
print("\n--- Map and Filter ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(): keeps only the items where the lambda returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (filter): {evens}")

# map(): transforms every item in the list using the lambda logic
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers (map): {squared}")