"""
Python Core - 06 Libraries (numpy)
Exercise 7: The Basic Stats Calculator (Easy - Fixation)
Folder: 07_basic_stats_calculator/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. You have an array representing the daily active users (DAU) of an app over 10 days:
   dau = np.array([120, 135, 150, 145, 180, 175, 190, 210, 205, 230])
3. Use standard NumPy functions to calculate and print:
   - The total sum of users across all 10 days.
   - The mean (average) DAU.
   - The median DAU.
   - The standard deviation of the DAU.
"""

import numpy as np 

dau = np.array([120, 135, 150, 145, 180, 175, 190, 210, 205, 230])

print(f"The total sum of users across all 10 days: {np.sum(dau)}")
print(f"The mean (average) DAU: {np.average(dau)}")
print(f"The median DAU: {np.median(dau)}")
print(f"The standard deviation of the DAU: {np.std(dau):.2f}")
