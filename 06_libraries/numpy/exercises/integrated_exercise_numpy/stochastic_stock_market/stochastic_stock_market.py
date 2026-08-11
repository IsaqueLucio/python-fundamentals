"""
Python Core - 06 Libraries (numpy)
Exercise 14: The Stochastic Stock Market (Hardcore - Random Walks & Axis Aggregation)
Folder: 14_stochastic_stock_market/
Main File: main.py

Scenario:
You are building a Monte Carlo simulator to project the future stock prices of 5 different tech companies over a full trading year (252 days). You must track their daily cumulative paths and identify the winner.

Rules:
1. Import 'numpy' as 'np'.
2. Set 'np.random.seed(999)'.
3. Step A (Simulating Daily Returns):
   - Generate a matrix of shape (252, 5) representing the daily percentage returns of 5 stocks.
   - Use 'np.random.normal()'. Assume a daily mean return of 0.001 (0.1%) and a standard deviation of 0.02 (2% volatility).
4. Step B (The Random Walk):
   - Stock prices compound. To get the price multiplier path, simply add 1 to the returns matrix, then calculate the CUMULATIVE PRODUCT down the days (axis=0) using 'np.cumprod()'.
   - Multiply the entire resulting matrix by 100 (assuming all 5 stocks started at a base price of $100 on Day 0).
   - Save this matrix as 'price_paths'.
5. Step C (Analysis via Axes):
   - Extract the FINAL prices of all 5 stocks (the last row of 'price_paths').
   - Use 'np.argmax()' to find the index of the stock with the highest final price.
   - Use 'np.max()' on the last row to find what that winning price was.
   - Calculate the daily market average (the mean price of all 5 stocks on each of the 252 days) using 'np.mean()' along the correct axis.
6. Print the winning stock index, its final price, and the final market average.
"""
#1
import numpy as np
#2
np.random.seed(999)
#3
daily_percentage_stocks = np.random.normal(loc=0.001, scale=0.02, size=(252, 5))
#4
daily_percentage_stocks += 1
price_paths = np.cumprod(daily_percentage_stocks, axis=0) * 100
#5
final_lines = price_paths[-1]
bigest_index = np.argmax(final_lines)
bigest_value = np.max(final_lines)
dps_mean = np.mean(price_paths, axis=1)
#6
print(f"Winning stock index:  {bigest_index}\n"
      f"Winning stock price:  {bigest_value:.2f}\n"
      f"Final Market Average: {dps_mean[-1]:.2f}\n")