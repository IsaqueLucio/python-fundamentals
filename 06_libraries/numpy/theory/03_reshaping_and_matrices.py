"""
Python Core - 06 Libraries
Module: numpy
File: 03_reshaping_and_matrices.py
Description: Mastering array reshaping, flattening, transposition, and matrix stacking.
"""
import numpy as np

print("--- 1. The Art of Reshaping ---")
# Reshaping changes the geometric structure of the data without changing the actual elements.
# Rule: The total number of elements must remain EXACTLY the same!

vector = np.arange(1, 13) # Creates a 1D array from 1 to 12. Shape: (12,)
print(f"Original 1D Vector:\n{vector}")

# Let's reshape it into a 2D matrix of 3 rows and 4 columns (3 * 4 = 12)
matrix_3x4 = vector.reshape(3, 4)
print(f"\nReshaped to 3x4 Matrix:\n{matrix_3x4}")

# The Magic '-1': If you know you want 2 rows, but don't want to calculate the columns, let NumPy do it!
matrix_2xN = vector.reshape(2, -1)
print(f"\nReshaped with '-1' (2 rows, automatic columns):\n{matrix_2xN}")
print("\n" + "="*60 + "\n")


print("--- 2. Flattening (Back to 1D) ---")
# Often, algorithms like Image Classification require turning a 2D/3D matrix back into a flat 1D array.
flat_array = matrix_3x4.flatten()
print(f"Flattened Matrix:\n{flat_array}")
print("\n" + "="*60 + "\n")


print("--- 3. Transposition (.T) ---")
# Transposing flips a matrix over its diagonal, switching rows and columns.
# Essential in linear algebra and manipulating dataset orientations.
print(f"Original 3x4:\n{matrix_3x4}")
print(f"\nTransposed 4x3 (.T):\n{matrix_3x4.T}")
print("\n" + "="*60 + "\n")


print("--- 4. Stacking and Concatenation ---")
# Joining multiple arrays together.
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Vertical Stack (Rows on top of rows) -> Axis 0
v_stack = np.vstack((A, B))
print(f"Vertical Stack (np.vstack):\n{v_stack}")

# Horizontal Stack (Columns next to columns) -> Axis 1
h_stack = np.hstack((A, B))
print(f"\nHorizontal Stack (np.hstack):\n{h_stack}")

# np.concatenate is the universal function for this, where you specify the axis!
# np.concatenate((A, B), axis=0) is the same as vstack.