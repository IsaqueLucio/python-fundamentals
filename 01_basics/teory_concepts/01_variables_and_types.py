# Variables and Types
# Explore Python's dynamic typing system and variable assignment

"""
Python Core - 01 Basics
File: 01_variables_and_types.py
Description: Demonstrating dynamic typing and basic data types in Python.
"""

# 1. Strings (Text)
# In Python, you can use either single or double quotes for strings.
user_name = "Isaque Lucio"
role = 'Back-end Developer'

# 2. Integers (Whole numbers)
# No need to declare 'int' before the variable, Python infers it automatically.
age = 20

# 3. Floats (Decimal numbers)
# Always use a dot for decimals, never a comma.
height = 1.70

# 4. Booleans (True or False)
# Unlike Java (true/false), Python booleans MUST start with an uppercase letter!
is_studying_python = True
is_rich = False

# 5. Printing values and checking their types
# The type() function is incredibly useful for debugging and checking what a variable holds.
print("--- User Info ---")
print("Name:", user_name, "| Type:", type(user_name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Studying Python:", is_studying_python, "| Type:", type(is_studying_python))
print("Is Rich:", is_rich, "| Type:", type(is_rich))
# 6. Dynamic Typing in Action
# A variable can completely change its type during execution without throwing errors.
print("\n--- Dynamic Typing ---")
dynamic_variable = 100
print("Dynamic Variable (initial):", dynamic_variable, "| Type:", type(dynamic_variable))

dynamic_variable = "Now I am a string!"
print("Dynamic Variable (changed):", dynamic_variable, "| Type:", type(dynamic_variable))