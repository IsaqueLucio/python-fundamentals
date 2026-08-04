"""
Python Core - 06 Libraries (numpy)
Exercise 6: The Tensor Transformation Engine (Hard - Architecture & Manipulation)
Folder: 06_tensor_transformation_engine/
Main File: main.py

Scenario:
You received a corrupted timeseries dataset. The data was recorded in the wrong orientation and dimensions. You must fix it using transpositions and dynamic reshaping before feeding it to the analytics engine.

Rules:
1. Import 'numpy' as 'np'.
2. Create the corrupted dataset using 'np.arange(1, 25)' and reshape it to a (6, 4) matrix:
   corrupted_data = np.arange(1, 25).reshape(6, 4)
3. Step A (Transposition):
   - The rows and columns are flipped! Transpose the matrix so it becomes (4, 6).
   - Save it as 'transposed_data' and print it.
4. Step B (The Magic Dimension):
   - The analytics engine requires the dataset to have exactly 3 columns, but it doesn't care how many rows it has.
   - Use '.reshape()' with the magic '-1' wildcard to force 'transposed_data' into an array with exactly 3 columns.
   - Save it as 'engine_ready_data' and print it.
5. Step C (Validation):
   - Print the '.shape' of 'engine_ready_data'. (If you did it right, it should automatically be (8, 3)).
   - Verify that the total number of elements remained perfectly conserved at 24!
"""

import numpy as np

corrupted_data = np.arange(1, 25).reshape(6, 4)
transposed_data = corrupted_data.T
print(f"Transposed data:\n{transposed_data}")
engine_ready_data = transposed_data.reshape(-1, 3)
print(f"Engine ready data:\n{engine_ready_data}")
print(f"Engine ready data shape: {engine_ready_data.shape}\n"
      f"Engine ready data number of elements: {engine_ready_data.size}")