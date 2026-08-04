"""
Python Core - 06 Libraries
Module: numpy
File: 04_statistics_and_aggregation.py
Description: Advanced statistical metrics, percentiles, index hunting, and safe aggregations.
"""
import numpy as np

print("--- 1. Basic Statistical Metrics ---")
# NumPy provides highly optimized C-based functions for standard statistics.
revenue = np.array([1200, 1500, 800, 2200, 3100, 1500, 950])

print(f"Total Revenue (Sum):      {np.sum(revenue)}")
print(f"Average Revenue (Mean):   {np.mean(revenue):.2f}")
print(f"Median Revenue (Median):  {np.median(revenue)}")
# Standard Deviation measures how spread out the numbers are from the mean
print(f"Standard Deviation (Std): {np.std(revenue):.2f}")
print(f"Variance (Var):           {np.var(revenue):.2f}")
print("\n" + "="*60 + "\n")


print("--- 2. Percentiles and Quartiles ---")
# Percentiles tell you the value below which a given percentage of observations fall.
# Great for finding outliers or defining thresholds (e.g., "Top 10%").
print(f"25th Percentile (Q1): {np.percentile(revenue, 25)}")
print(f"75th Percentile (Q3): {np.percentile(revenue, 75)}")
# The 90th percentile means 90% of the data is below this value
print(f"90th Percentile:      {np.percentile(revenue, 90)}")
print("\n" + "="*60 + "\n")


print("--- 3. Index Hunters (argmax & argmin) ---")
# Sometimes finding the maximum value isn't enough; you need to know WHERE it is.
# argmax() returns the INDEX of the maximum value.
max_value = np.max(revenue)
best_month_index = np.argmax(revenue)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]

print(f"Highest Revenue was {max_value}.")
print(f"It happened at index {best_month_index}, which is {months[best_month_index]}.")

worst_month_index = np.argmin(revenue)
print(f"Lowest Revenue was {np.min(revenue)} in {months[worst_month_index]}.")
print("\n" + "="*60 + "\n")


print("--- 4. Safe Aggregations (Handling NaNs) ---")
# Real data is messy. np.nan (Not a Number) represents missing data in numeric arrays.
corrupted_sensor_data = np.array([22.5, 23.1, np.nan, 22.8, np.nan, 24.0])

# Normal math functions CRASH (return NaN) if there is even a single NaN in the array!
print(f"Normal Mean (Fails): {np.mean(corrupted_sensor_data)}")

# The 'nan-' family of functions ignores NaNs automatically.
print(f"Safe Mean (nanmean): {np.nanmean(corrupted_sensor_data):.2f}")
print(f"Safe Sum (nansum):   {np.nansum(corrupted_sensor_data):.2f}")
print(f"Safe Max (nanmax):   {np.nanmax(corrupted_sensor_data)}")