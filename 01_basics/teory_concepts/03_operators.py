# Operators
# Arithmetic, comparison, logical, and assignment operators

"""
Python Core - 01 Basics
File: 03_operators.py
Description: Arithmetic, comparison, logical, and assignment operators.
"""

# 1. Arithmetic Operators
print("--- Arithmetic Operators ---")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")    # Addition
print(f"{a} - {b} = {a - b}")    # Subtraction
print(f"{a} * {b} = {a * b}")    # Multiplication
print(f"{a} / {b} = {a / b}")    # Standard Division (ALWAYS returns a float: 3.333...)

# Python specific operators:
print(f"{a} // {b} = {a // b}")  # Integer Division (Drops the decimal part: 3)
print(f"{a} % {b} = {a % b}")    # Modulo (Remainder of the division: 1)
print(f"{a} ** {b} = {a ** b}")  # Exponentiation (10 to the power of 3: 1000)

# 2. Assignment Operators 
# Note: Python DOES NOT have ++ or -- operators like Java.
print("\n--- Assignment Operators ---")
counter = 5
print(f"Initial counter: {counter}")

counter += 1  # Equivalent to: counter = counter + 1 (Java's counter++)
print(f"After counter += 1: {counter}")

counter *= 2  # Equivalent to: counter = counter * 2
print(f"After counter *= 2: {counter}")

# 3. Comparison Operators
# They compare values and always return a boolean (True or False)
print("\n--- Comparison Operators ---")
x = 10
y = 20
print(f"{x} == {y}: {x == y}")  # Equal to
print(f"{x} != {y}: {x != y}")  # Not equal to
print(f"{x} >= 10: {x >= 10}")  # Greater than or equal to

# 4. Logical Operators
# Python uses readable English words instead of symbols like &&, ||, or !
print("\n--- Logical Operators ---")
is_adult = True
has_license = False

# AND: Both sides must be True
can_drive = is_adult and has_license
print(f"is_adult and has_license: {can_drive}")

# OR: At least one side must be True
needs_bus_pass = not is_adult or not has_license
print(f"needs_bus_pass: {needs_bus_pass}")

# NOT: Inverts the boolean value
print(f"not has_license: {not has_license}")