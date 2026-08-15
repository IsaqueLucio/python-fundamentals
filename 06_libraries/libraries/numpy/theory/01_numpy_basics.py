"""
Python Core - 06 Libraries
Module: numpy
File: 01_numpy_basics.py
Description: Understanding N-dimensional arrays, vectorization, and basic statistics.
"""
import numpy as np
import time

print("--- 1. Arrays vs Lists: The Basics ---")
# Creating a 1D Array (Vector)
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(f"Python List: {my_list}")
print(f"NumPy Array: {my_array}")
print(f"Array Type: {type(my_array)}\n")

# Creating a 2D Array (Matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("2D Matrix:")
print(matrix)
print(f"Shape of matrix: {matrix.shape}") # Returns (rows, columns)
print(f"Number of dimensions: {matrix.ndim}\n")


print("--- 2. The Power of Vectorization ---")
# If you want to multiply all elements by 2 in a normal list, you need a for-loop.
# In NumPy, you apply the operation directly to the entire array!

prices = np.array([10.0, 25.5, 30.0, 50.0])
discounted_prices = prices * 0.8  # Applies 20% discount to ALL elements instantly

print(f"Original Prices:   {prices}")
print(f"Discounted Prices: {discounted_prices}\n")


print("--- 3. Array Slicing and Filtering (Boolean Indexing) ---")
numbers = np.array([10, 15, 20, 25, 30, 35, 40])

print(f"First 3 elements: {numbers[:3]}")
print(f"Last 2 elements: {numbers[-2:]}")

# Boolean Indexing: Filtering data without loops!
# This creates a mask [False, False, False, False, True, True, True] and applies it.
high_numbers = numbers[numbers > 25]
print(f"Numbers greater than 25: {high_numbers}\n")


print("--- 4. Built-in Math and Statistics ---")
sales = np.array([120, 150, 90, 200, 130])

print(f"Total Sales (Sum): {np.sum(sales)}")
print(f"Average Sales (Mean): {np.mean(sales)}")
print(f"Highest Sale (Max): {np.max(sales)}")
print(f"Lowest Sale (Min): {np.min(sales)}\n")


print("--- 5. Performance Proof ---")
# Let's add two lists of 1 million items together.
SIZE = 1_000_000
list_a = list(range(SIZE))
list_b = list(range(SIZE))

array_a = np.arange(SIZE) # np.arange is NumPy's version of range()
array_b = np.arange(SIZE)

# Standard Python Loop
start_time = time.time()
list_c = [list_a[i] + list_b[i] for i in range(SIZE)]
print(f"Standard Python List time: {time.time() - start_time:.4f} seconds")

# NumPy Vectorized Addition
start_time = time.time()
array_c = array_a + array_b
print(f"NumPy Array time:          {time.time() - start_time:.4f} seconds")