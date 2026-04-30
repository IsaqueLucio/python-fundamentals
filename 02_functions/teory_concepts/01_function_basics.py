"""
Python Core - 02 Functions
File: 01_function_basics.py
Description: Introduction to function definition, calling, and variable scope.
"""

# 1. Defining a Basic Function
# In Python, we use the 'def' keyword (short for define) to create a function.
# The code block inside the function only runs when the function is explicitly called.
print("--- Basic Functions ---")

def greet():
    print("Hello! Welcome to the functions module.")

# Calling the function
greet()

# 2. Functions with Parameters
# Parameters allow us to pass data into the function to make it dynamic.
print("\n--- Functions with Parameters ---")

def greet_user(name):
    print(f"Hello, {name}! Good to see you.")

greet_user("Isaque")
greet_user("Alice")

# 3. Default Parameters
# You can assign a default value to a parameter. 
# If the user doesn't provide an argument when calling the function, the default is used.
# This eliminates the need for "Method Overloading" like in Java.
print("\n--- Default Parameters ---")

def show_profile(name, role="Developer"):
    print(f"Name: {name} | Role: {role}")

# Uses the default role because the second argument is missing
show_profile("Isaque")                     

# Overrides the default role with the provided string
show_profile("Bob", "Data Scientist")      

# 4. Variable Scope (Local vs Global)
# Variables created inside a function are 'local' and cannot be accessed outside of it.
print("\n--- Variable Scope ---")

global_variable = "I am accessible everywhere!"

def test_scope():
    local_variable = "I only exist inside this function!"
    
    # The function can read variables created outside of it
    print(f"Reading global: {global_variable}")
    print(f"Reading local: {local_variable}")

test_scope()

# If you uncomment the line below, Python will crash with a NameError
# because 'local_variable' is destroyed as soon as the function finishes running.
# print(local_variable)