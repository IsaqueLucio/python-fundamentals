"""
Python Core - 06 Libraries
Module: numpy
File: 05_random_and_simulations.py
Description: Mastering pseudo-random number generation, statistical distributions, and reproducibility (seeds).
"""
import numpy as np

print("--- 1. Reproducibility (The Seed) ---")
# If you are testing a Machine Learning model, you want the "randomness" to be the same every time you run the script.
# We do this by setting a seed. (42 is a cultural joke/standard in programming).
np.random.seed(42)
print("Seed set to 42. Random numbers are now deterministic!")
print("\n" + "="*60 + "\n")


print("--- 2. Basic Random Arrays ---")
# np.random.rand: Generates floats between 0 and 1.
random_floats = np.random.rand(3) # Array of 3 items
print(f"Random Floats (0 to 1): {random_floats}")

# np.random.randint: Generates integers between [low, high)
random_integers = np.random.randint(1, 100, size=(2, 5)) # 2 rows, 5 columns
print(f"\nRandom Integers (1 to 99) in a 2x5 matrix:\n{random_integers}")
print("\n" + "="*60 + "\n")


print("--- 3. Statistical Distributions (The Core of AI) ---")
# 3.1 Uniform Distribution: Every number has an EQUAL chance of appearing.
uniform_data = np.random.uniform(low=10.0, high=50.0, size=5)
print(f"Uniform Distribution (10 to 50): {uniform_data}")

# 3.2 Normal (Gaussian) Distribution: The famous "Bell Curve". 
# Most numbers are clustered around the mean.
# Parameters: loc (mean), scale (standard deviation), size
# Simulating the heights of 5 people (Mean: 1.75m, Std Dev: 0.15m)
normal_data = np.random.normal(loc=1.75, scale=0.15, size=5)
print(f"\nNormal Distribution (Heights in meters): {normal_data}")
print("\n" + "="*60 + "\n")


print("--- 4. Shuffling and Choosing ---")
# np.random.choice: Great for sampling data or simulating categorical events.
colors = ["Red", "Blue", "Green", "Yellow"]
# Simulating 10 random pulls from a bag of colors (with replacement)
random_pulls = np.random.choice(colors, size=10)
print(f"10 Random Pulls: {random_pulls}")

# np.random.shuffle: Modifies a sequence IN-PLACE (shuffles like a deck of cards)
deck = np.arange(1, 11)
print(f"\nOriginal Deck: {deck}")
np.random.shuffle(deck)
print(f"Shuffled Deck: {deck}")