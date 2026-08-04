"""
Python Core - 06 Libraries (numpy)
Exercise 5: The Dataset Stacker (Intermediate - Logic & Integration)
Folder: 05_dataset_stacker/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. You are combining data from two different servers into a single Machine Learning dataset.
3. Define the existing datasets (Features: Age, Salary, Credit Score):
   server1_data = np.array([[25, 5000, 700],
                            [30, 7000, 750]])
   server2_data = np.array([[45, 9000, 800],
                            [22, 3000, 600]])
4. Step A (Vertical Integration):
   - Combine both matrices into a single matrix called 'full_features' by stacking them VERTICALLY.
   - Print the resulting 'full_features' matrix (it should have 4 rows and 3 columns).
5. Step B (Horizontal Integration):
   - The marketing team sent a new column representing the "Label" (Did the customer buy the product? 1=Yes, 0=No).
   - labels = np.array([1, 0, 1, 0])
   - BEFORE you can stack this column horizontally next to 'full_features', you MUST transform 'labels' from a 1D vector (4,) into a 2D column vector (4, 1) using '.reshape(-1, 1)'.
   - After reshaping, use 'np.hstack' to attach the labels to the right side of 'full_features'.
   - Print the final dataset!
"""

import numpy as np

server1_data = np.array([[25, 5000, 700],
                         [30, 7000, 750]])
server2_data = np.array([[45, 9000, 800],
                         [22, 3000, 600]])
full_features = np.vstack((server1_data, server2_data))
print(f"Full features:\n{full_features}")
labels = np.array([1, 0, 1, 0])
flat_labels = labels.flatten().reshape(-1, 1)
final_features = np.hstack((full_features, flat_labels))
print(f"Final Features: \n{final_features}")