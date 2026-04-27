# Conditionals
# if, elif, else statements for decision making

"""
Python Core - 01 Basics
File: 04_conditionals.py
Description: Decision making using if, elif, and else statements.
"""

# 1. Simple If / Else
# Parentheses around the condition are optional and rarely used in Python.
# The colon (:) indicates the start of a new code block.
print("--- Simple If/Else ---")
age = 20

if age >= 18:
    # This line is indented, meaning it belongs inside the 'if' block
    print("Status: Adult. You are allowed to enter.")
else:
    # This line belongs inside the 'else' block
    print("Status: Minor. Access denied.")

# 2. The Elif Chain (Else If)
# Used to check multiple conditions sequentially.
print("\n--- Elif Chain ---")
account_balance = 500.0
withdrawal_amount = 600.0

if withdrawal_amount <= 0:
    print("Transaction failed: Invalid amount.")
elif withdrawal_amount <= account_balance:
    print(f"Transaction successful: Withdrew ${withdrawal_amount}.")
    account_balance -= withdrawal_amount
else:
    print("Transaction failed: Insufficient funds.")

# 3. Nested Conditionals
# You can place an if inside another if, just increase the indentation.
print("\n--- Nested Conditionals ---")
user_role = "admin"
is_active = True

if is_active:
    print("User is active.")
    if user_role == "admin":
        print("Access granted: Full system dashboard.")
    else:
        print("Access granted: Standard user view.")
else:
    print("Account is deactivated. Please contact support.")

# 4. The Ternary Operator (One-line if/else)
# A clean way to assign a value based on a condition (similar to Java's condition ? true : false)
print("\n--- Ternary Operator ---")
temperature = 35
# Syntax: [value_if_true] if [condition] else [value_if_false]
weather_status = "Hot" if temperature > 30 else "Normal"
print(f"The weather is {weather_status}.")