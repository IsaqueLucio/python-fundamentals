"""
Python Core - 05 Advanced
File: 01_modules_and_packages.py
Description: Understanding __name__, __main__, and Package structures.
"""

print("--- 1. The Magic Variable: __name__ ---")
# Every Python file has a built-in hidden variable called __name__.
# - If you run the file DIRECTLY, Python sets __name__ to "__main__".
# - If you IMPORT the file into another script, Python sets __name__ to the file's actual name.

print(f"Right now, the __name__ of this file is: '{__name__}'")


print("\n--- 2. The Execution Guard (if __name__ == '__main__') ---")
# This is a critical pattern in Python. 
# It prevents code from running accidentally when a file is imported somewhere else.

def helper_function():
    return "I am a helpful tool."

# We put tests and execution logic inside this block.
if __name__ == "__main__":
    print("This file is being run directly by the user!")
    print(f"Testing the function: {helper_function()}")
    # If another file imports this one (e.g., 'import 01_modules_and_packages'), 
    # EVERYTHING inside this 'if' block will be IGNORED. 
    # This keeps your modules safe and reusable!


print("\n--- 3. What is a Package? ---")
"""
A Module is a single .py file.
A Package is a FOLDER containing multiple .py files AND a special file called __init__.py.

Example Structure:
my_project/
├── main.py
└── payments/               <-- This is a Package!
    ├── __init__.py         <-- Tells Python: "Treat this folder as a package"
    ├── credit_card.py      <-- This is a Module inside the package
    └── paypal.py           <-- This is another Module

How to import from a package:
from payments.credit_card import process_payment
from payments import paypal
"""
print("In modern Python (3.3+), the __init__.py can be empty or even omitted, but it's a best practice to keep it to mark the folder as a package explicitly.")