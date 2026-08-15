"""
Python Core - 06 Libraries (numpy)
Exercise 9: The Corrupted Data Analyzer (Hard - Problem Solving & Safe Aggregations)
Folder: 09_corrupted_data_analyzer/
Main File: main.py

Scenario:
You received temperature readings from an IoT weather station, but the sensor malfunctioned several times, transmitting null data (NaN).

Rules:
1. Import 'numpy' as 'np'.
2. Create the corrupted dataset:
   temperatures = np.array([22.5, 23.0, np.nan, 24.1, 25.5, np.nan, 21.0, np.nan, 26.2, 25.8])
3. Step A (The Failure):
   - Calculate the standard mean using 'np.mean()' and print it. (Observe that it returns NaN).
4. Step B (The Safe Extraction):
   - Use the appropriate 'nan-' function to calculate the SAFE MEAN, ignoring the corrupted data.
   - Use the appropriate 'nan-' function to find the maximum valid temperature.
   - Use the appropriate 'nan-' function to find the minimum valid temperature.
5. Step C (Percentile Challenge):
   - NumPy has a safe version for percentiles too! Use 'np.nanpercentile(array, q)' to calculate the 75th percentile (Q3) of the valid temperatures.
6. Print a clean summary report containing the Safe Mean, Max, Min, and 75th Percentile!
"""

import numpy as np

temperatures = np.array([22.5, 23.0, np.nan, 24.1, 25.5, np.nan, 21.0, np.nan, 26.2, 25.8])
print(f"Trying to get the mean of the corrupted data temperature(MUST FAIL): {np.mean(temperatures)}")
print(f"Using the appropriate 'nan-' function to calculate the SAFE MEAN, ignoring the corrupted data: {np.nanmean(temperatures):.2f}\n"
      f"Using the appropriate 'nan-' function to find the maximum valid temperature: {np.nanmax(temperatures)}\n"
      f"Using the appropriate 'nan-' function to find the minimum valid temperature: {np.nanmin(temperatures)}\n"
      f"Using the appropriate 'nan-' function to find the 75th percentile (Q3) of the valid temperatures: {np.nanpercentile(temperatures, 75)}")



