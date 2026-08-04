"""
Python Core - 06 Libraries (numpy)
Exercise 8: The Index Hunter (Intermediate - Logic & Interpretation)
Folder: 08_index_hunter/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. You are tracking the stock prices of a company over 7 days.
   prices = np.array([150.5, 148.2, 155.0, 160.8, 158.4, 165.2, 162.1])
   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
3. Do NOT just find the max/min values. You must find the EXACT DAY they occurred!
4. Use 'np.argmax()' to find the index of the highest price and use it to print the day and the price.
   Example: "Highest price was 165.2 on Sat."
5. Use 'np.argmin()' to find the index of the lowest price and use it to print the day and the price.
"""

import numpy as np

prices = np.array([150.5, 148.2, 155.0, 160.8, 158.4, 165.2, 162.1])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

hp = np.argmax(prices)
hd = days[hp]
print(f"Highest Revenue was {np.max(prices)}.")
print(f"It happened at index {hp}, which is {days[hp]}.")

lp = np.argmin(prices)
ld = days[lp]
print(f"Lowest Revenue was {np.min(prices)}.")
print(f"It happened at index {lp}, which is {days[lp]}.")