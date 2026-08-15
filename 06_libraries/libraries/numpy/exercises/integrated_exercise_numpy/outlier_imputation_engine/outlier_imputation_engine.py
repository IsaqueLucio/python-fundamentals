"""
Python Core - 06 Libraries (numpy)
Exercise 13: The Outlier Imputation Engine (Hardcore - Safe Aggregations & Boolean Masking)
Folder: 13_outlier_imputation_engine/
Main File: main.py

Scenario:
A server logged the response times of 100,000 requests. However, 
system glitches introduced both missing values (NaNs) and extreme outliers (e.g., negative response times or times exceeding physical limits). 
You must clean this data using statistical thresholds without using a single loop.

Rules:
1. Import 'numpy' as 'np'.
2. Generate the corrupted dataset (Seed: 42):
   np.random.seed(42)
   response_times = np.random.normal(loc=150.0, scale=30.0, size=100000)
   # Introduce NaNs and extreme Outliers manually
   response_times[np.random.choice(100000, 5000, replace=False)] = np.nan
   response_times[np.random.choice(100000, 1000, replace=False)] = 9999.9
   response_times[np.random.choice(100000, 1000, replace=False)] = -500.0
3. Step A (Statistical Thresholds):
   - Calculate Q1 (25th percentile) and Q3 (75th percentile) safely using 'np.nanpercentile()'.
   - Calculate the Interquartile Range (IQR = Q3 - Q1).
   - Define the valid bounds: lower_bound = Q1 - (1.5 * IQR) and upper_bound = Q3 + (1.5 * IQR).
4. Step B (Boolean Vectorization):
   - Create a boolean mask identifying ALL invalid data: values that are NaN (using 'np.isnan()') OR values 
   below the lower_bound OR values above the upper_bound.
5. Step C (Safe Imputation):
   - Calculate the SAFE MEDIAN of the dataset (ignoring the invalid values). 
   Hint: you might want to temporarily convert bounds outliers to NaN to use 'np.nanmedian()', or use boolean 
   indexing to get the median of only the valid numbers.
   - Use 'np.where()' to replace all invalid data in 'response_times' with this safe median.
6. Validation:
   - Print the original corrupted mean vs the final cleaned mean, and confirm there are 0 NaNs left.
"""
import numpy as np

np.random.seed(42)

response_times = np.random.normal(loc=150.0, scale=30.0, size=100000)

response_times[np.random.choice(100000, 5000, replace=False)] = np.nan
response_times[np.random.choice(100000, 1000, replace=False)] = 9999.9
response_times[np.random.choice(100000, 1000, replace=False)] = -500.0

Q1 = np.nanpercentile(response_times, 25)
Q3 = np.nanpercentile(response_times, 75)
IQR = Q3 - Q1
lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

boolean_mask = np.isnan(response_times) | (response_times > upper_bound) | (response_times < lower_bound)

safe_median = np.median(response_times[~boolean_mask])
cleaned_response_times = np.where(boolean_mask, safe_median, response_times)

# Validation
corrupted_mean = np.nanmean(response_times)
cleaned_mean = np.mean(cleaned_response_times)
remaining_nans = np.isnan(cleaned_response_times).sum()

print(f"Corrupted mean: {corrupted_mean:.2f}")
print(f"Cleaned mean: {cleaned_mean:.2f}")
print(f"Remaining NaNs: {remaining_nans}")
