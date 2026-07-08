"""
Exercise 2: Your First Package
Main File: main.py
Dependencies to create: A FOLDER called 'ecommerce', and inside it: __init__.py, products.py, cart.py

--- Rules for the 'ecommerce' folder ---
1. Create a folder named 'ecommerce'.
2. Inside 'ecommerce', create an empty file named '__init__.py'. (This tells Python: "I am a package!").
3. Inside 'ecommerce', create 'products.py'.
   - Add a function 'get_catalog()' returning a simple list of 3 product strings.
4. Inside 'ecommerce', create 'cart.py'.
   - Add a function 'calculate_total(prices: list) -> float' returning the sum of the list.

--- Rules for 'main.py' (This file) ---
1. This file must be OUTSIDE the 'ecommerce' folder (in the same folder that contains the 'ecommerce' folder).
2. Import the products module: from ecommerce import products
3. Import the specific calculate_total function: from ecommerce.cart import calculate_total
4. Call 'products.get_catalog()' and print the result.
5. Create a fake list of prices (e.g., [10.5, 20.0, 5.0]) and pass it to 'calculate_total()', printing the result.
"""

from ecommerce import products
from ecommerce.cart import calculate_total

print(products.get_catalog())
prices = [10.5, 20.0, 5.0]
print(calculate_total(prices))