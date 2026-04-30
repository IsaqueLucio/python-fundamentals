"""
Python Core - 02 Functions
File: 02_parameters_and_return.py
Description: Returning values, type hinting, and dynamic parameters (*args and **kwargs).
"""

# 1. The 'return' Keyword
# Unlike print(), return actually passes the data back to the caller so it can be saved or used.
print("--- Return Statement ---")

def calculate_area(width, height):
    area = width * height
    return area  # Devolve o valor para quem chamou a função

# Saving the returned value into a variable
living_room_area = calculate_area(5.0, 4.0)
print(f"The living room area is {living_room_area} sqm.")

# 2. Type Hinting (A bridge for Java developers)
# Python is dynamic, but you can add "hints" to tell the IDE what types to expect.
# Format: param_name: type -> return_type
print("\n--- Type Hinting ---")

def format_price(value: float, currency: str = "R$") -> str:
    return f"{currency} {value:.2f}"

price_tag = format_price(150.5)
print(f"Formatted price: {price_tag}")

# 3. Dynamic Positional Parameters (*args)
# The '*' packs any number of positional arguments into a Tuple (a read-only list).
print("\n--- *args (Dynamic Positional) ---")

def calculate_total(*prices):
    # 'prices' is now a tuple containing all the numbers passed to the function
    # sum() is a built-in Python function that adds everything in a collection
    return sum(prices)

print(f"Total of 3 items: {calculate_total(10, 20, 30)}")
print(f"Total of 5 items: {calculate_total(5, 5, 10, 10, 20)}")

# 4. Dynamic Keyword Parameters (**kwargs)
# The '**' packs any number of named arguments into a Dictionary (key-value pairs).
# Extremely common in libraries like Django and Pandas.
print("\n--- **kwargs (Dynamic Keyword) ---")

def create_user(name, **user_info):
    print(f"Creating profile for: {name}")
    
    # 'user_info' is a dictionary containing all the extra named arguments
    for key, value in user_info.items():
        print(f" - {key.capitalize()}: {value}")

# Calling the function with a dynamic amount of named parameters
create_user("Isaque", role="Admin", department="IT", active=True)
print("")
create_user("Alice", role="Developer", language="Python")