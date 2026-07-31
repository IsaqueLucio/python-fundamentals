"""
Python Core - 06 Libraries (numpy)
Exercise 1: The Inventory Broadcaster (Easy - Fixation)
Folder: 01_inventory_broadcasting/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. Create a 2D array representing the stock of 4 different products (columns) across 3 different stores (rows):
   stock_data = np.array([
       [10, 50, 30, 20],  # Store A
       [ 5, 20, 10, 15],  # Store B
       [40, 10, 60,  0]   # Store C
   ])
3. Axis Manipulation:
   - Calculate and print the TOTAL items in stock for EACH STORE (Hint: collapse the columns using axis=1).
   - Calculate and print the TOTAL items in stock for EACH PRODUCT (Hint: collapse the rows using axis=0).
4. Broadcasting:
   - The company decided to ship exactly 5 extra units of EACH product to EVERY store.
   - Without using any loops, create a new array 'updated_stock' by simply adding 5 to 'stock_data'.
   - Print the 'updated_stock' matrix to prove broadcasting worked!
"""

import numpy as np

stock_data = np.array([
   [10, 50, 30, 20],  # Store A
   [ 5, 20, 10, 15],  # Store B
   [40, 10, 60,  0]   # Store C
])

print(f"TOTAL items in stock for EACH STORE: \n{np.sum(stock_data, axis=1)}")
print(f"TOTAL items in stock for EACH PRODUCT: \n{np.sum(stock_data, axis=0)}")
updated_stock = stock_data+5
print(f"Updated stock: \n{updated_stock}")