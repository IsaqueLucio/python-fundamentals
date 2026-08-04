"""
Python Core - 06 Libraries (numpy)
Exercise 4: The Image Flattener (Easy - Fixation)
Folder: 04_image_flattener/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. In Computer Vision, black-and-white images are just 2D matrices of pixel intensities.
   Create a 4x4 matrix simulating a tiny image using np.arange(16).reshape(4, 4):
   image_matrix = np.arange(16).reshape(4, 4)
3. Step A (Reshaping):
   - The AI model requires the image to be processed in 2 rows of 8 pixels.
   - Use '.reshape()' to convert 'image_matrix' into a 2x8 matrix and print it.
4. Step B (Flattening):
   - Another simpler algorithm requires a single 1D vector of pixels.
   - Use '.flatten()' on the ORIGINAL 'image_matrix' to convert it into a 1D array.
   - Print the flattened array and verify its shape using '.shape'.
"""

import numpy as np

image_matrix = np.arange(16).reshape(4, 4)
matrix_2x8 = image_matrix.reshape(2, 8)
vector_1d = image_matrix.flatten()

print(f"Matrix 4x4:\n{image_matrix}\n"
      f"Matrix 2x8:\n{matrix_2x8}\n"
      f"Vector 1D:\n{vector_1d}\n"
      f"Vector 1D shape:\n{vector_1d.shape}")
