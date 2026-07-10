"""
Python Core - 05 Advanced
File: 02_error_handling.py
Description: Intercepting and handling errors using try, except, else, and finally.
"""

print("--- 1. The Basic Try/Except ---")
# We put the "dangerous" code inside the 'try' block.
try:
    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number
    print(f"The result is {result}")

# We specify exactly WHICH error we are anticipating.
except ZeroDivisionError:
    print("ERROR: You cannot divide by zero! The universe would implode.")
except ValueError:
    print("ERROR: That's not a valid number! Please type digits, not letters.")


print("\n--- 2. The Complete Structure (try/except/else/finally) ---")
# A more robust scenario mimicking a database or file operation
def process_data(data_list, index):
    try:
        print(f"Attempting to access index {index}...")
        value = data_list[index]
    
    except IndexError:
        # Runs ONLY if the specific error occurs
        print("CRITICAL: Index out of bounds. The data does not exist.")
    
    except Exception as e:
        # A generic catch-all for any other unexpected error (use sparingly!)
        print(f"CRITICAL: An unexpected error occurred: {e}")
    
    else:
        # Runs ONLY if the 'try' block succeeds (no errors happened)
        print(f"SUCCESS: Data retrieved successfully -> {value}")
        # This is where we would normally do the heavy lifting with the data
    
    finally:
        # Runs ALWAYS, no matter if there was an error or not.
        # This is crucial for closing files or database connections so they don't leak memory.
        print("CLEANUP: Closing connection to the data source.\n")


# Let's test the complete structure
sample_data = ["Alice", "Bob", "Charlie"]

# Test A: Success
process_data(sample_data, 1)

# Test B: Expected Error
process_data(sample_data, 99)


print("--- 3. Forcing an Error (raise) ---")
# Sometimes the code is correct for Python, but it violates our business rules.
# We use 'raise' to create our own error manually.

def create_password(password: str):
    if len(password) < 6:
        # We raise the red flag manually!
        raise ValueError("The password must be at least 6 characters long.")
    return "Password saved successfully!"

try:
    print(create_password("123"))
except ValueError as e:
    # We catch the exact message we created in the 'raise' statement
    print(f"SECURITY ERROR: {e}")