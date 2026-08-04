"""
Python Core - 06 Libraries (numpy)
Exercise 10: The Seed and the Dice (Easy - Fixation)
Folder: 10_seed_and_dice/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. Set the random seed to 42 to ensure reproducibility.
3. Simulate rolling a standard 6-sided die 10 times using 'np.random.randint'. 
   (Hint: Remember the high bound in randint is exclusive!).
   - Print the resulting array of the 10 dice rolls.
4. Simulate the daily average temperatures of a city for 7 days using 'np.random.normal'.
   - Assume the mean (loc) is 25.0 degrees Celsius and the standard deviation (scale) is 2.0.
   - Print the array of temperatures.
"""

import numpy as np

np.random.seed(42)
dice_rolls = np.random.randint(1, 7, size=10)
for i, dice in enumerate(dice_rolls):
    print(f"Roll {i+1}, dice face: {dice}")
print("")
city_temperatures = np.random.normal(loc = 25.0,scale=2.0, size=7)
print(f"City temperatures: {city_temperatures}")