"""
Python Core - 06 Libraries (numpy)
Exercise 1: The Array Transformer (Easy - Fixation)
Folder: 01_array_transformer/
Main File: array_transformer.py

Rules:
1. Import the 'numpy' module as 'np'.
2. Create a standard Python list of 5 product prices: [15.50, 20.00, 35.75, 10.00, 50.25].
3. Convert this list into a NumPy array called 'prices_array'.
4. Apply a 15% tax to all prices at once using vectorization (multiply the array by 1.15) and store it in 'taxed_prices'.
5. Print the original array and the new 'taxed_prices' array.
6. Use NumPy's built-in statistical functions to calculate and print:
   - The maximum price in the new array.
   - The minimum price in the new array.
   - The average (mean) price of the new array.
"""

import numpy as np

product_prices = [15.50, 20.00, 35.75, 10.00, 50.25]
prices_array = np.array(product_prices)

taxed_prices = prices_array * 1.15

print(f"Original Prices:   {prices_array}")
print(f"Discounted Prices: {taxed_prices}\n")

print(f"Average price (Mean): {np.mean(taxed_prices):.2f}")
print(f"Highest price (Max): {np.max(taxed_prices):.2f}")
print(f"Lowest price (Min): {np.min(taxed_prices):.2f}\n")