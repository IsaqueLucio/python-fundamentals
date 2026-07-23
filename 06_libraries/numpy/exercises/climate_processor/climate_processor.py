"""
Python Core - 06 Libraries (numpy)
Exercise 3: The Climate Data Processor (Hard - Problem Solving)
Folder: 03_climate_processor/
Main File: climate_processor.py

Rules:
1. Import 'numpy' as 'np'.
2. Create an array representing 30 days of daily temperatures in Celsius:
   temperatures = np.array([
       22.5, 23.0, 25.1, 28.4, 30.2, 32.0, 35.5, 36.1, 38.0, 34.2,
       29.0, 25.5, 21.0, 19.5, 18.0, 15.5, 12.0, 10.5,  9.0,  8.5,
       11.0, 14.2, 16.5, 20.0, 22.1, 24.5, 26.0, 28.5, 31.0, 33.5
   ])
3. A climate anomaly is defined as a temperature below 15.0 OR above 35.0. 
   Create a boolean mask using the bitwise OR operator '|' (syntax: (condition_1) | (condition_2)) 
   and use it to extract all anomalous temperatures into a new array called 'anomalies'.
4. Print the total NUMBER of anomalous days found (hint: use the 'len()' function or '.size' attribute).
5. Convert the entire original 'temperatures' array from Celsius to Fahrenheit using vectorization.
   (Formula: F = C * 1.8 + 32). Store this in a new array called 'temperatures_f'.
6. Find the hottest day of the month in Fahrenheit. 
   Use the 'np.argmax(array)' function to find the exact index (day) this peak temperature occurred.
7. Print a final report containing:
   - The average temperature of the month (in Celsius).
   - The array of anomalous temperatures (in Celsius).
   - The hottest temperature in Fahrenheit and the exact day (index + 1) it happened.
"""

import numpy as np

temperatures = np.array([
       22.5, 23.0, 25.1, 28.4, 30.2, 32.0, 35.5, 36.1, 38.0, 34.2,
       29.0, 25.5, 21.0, 19.5, 18.0, 15.5, 12.0, 10.5,  9.0,  8.5,
       11.0, 14.2, 16.5, 20.0, 22.1, 24.5, 26.0, 28.5, 31.0, 33.5
   ])

print(f"\nTemperatures in celsius: \n{temperatures}\n")
climate_anomaly = (temperatures < 15) | (temperatures > 35)
anomalous_climate = temperatures[climate_anomaly]
print(f"Total number of anomalous days found: {len(anomalous_climate)}\n")
temparatures_f = temperatures * 1.8 + 32
print(f"Temperatures converted from Celsius to Fahrenheit: \n{temparatures_f}")
hottest_temparature = np.max(temparatures_f)
hottest_day = np.where(temparatures_f == hottest_temparature)[0][0]+1
print("\nFinal report: \n"
      f"The average temperature of the month (in Celsius): {np.mean(temperatures):.2f}\n"
      f"The array of anomalous temperatures (in Celsius):\n{anomalous_climate}\n"
      f"The hottest temperature in Fahrenheit and the exact day:\n"
      f"Hottest day: {hottest_day}\n"
      f"Hottest temparature: {hottest_temparature}")