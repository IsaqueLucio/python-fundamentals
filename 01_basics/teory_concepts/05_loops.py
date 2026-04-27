# Loops
# for and while loops for iteration

"""
Python Core - 01 Basics
File: 05_loops.py
Description: Iteration and repeating tasks using for and while loops.
"""

# 1. The While Loop
# Executes a block of code as long as a condition is True.
# The syntax and behavior are practically identical to Java.
print("--- While Loop ---")
counter = 0
while counter < 3:
    print(f"While loop iteration: {counter}")
    counter += 1  # Remember: no counter++ in Python!

# 2. The For Loop and range()
# Python iterates over sequences. To run a loop a specific number of times,
# we use the built-in range() function.
print("\n--- For Loop with range() ---")

# range(stop): Generates numbers from 0 up to (but not including) stop.
print("Using range(3):")
for i in range(3):
    print(f"Iteration: {i}")

# range(start, stop, step): Equivalent to Java's (int i = 2; i < 11; i += 2)
print("\nUsing range(start, stop, step):")
for num in range(2, 11, 2):
    print(f"Even number: {num}")

# 3. Loop Control: break and continue
# These keywords behave exactly as they do in Java.
print("\n--- Break and Continue ---")
for i in range(1, 6):
    if i == 3:
        print("Skipping number 3 (continue)")
        continue  # Skips the rest of this iteration
    
    if i == 5:
        print("Stopping loop at 5 (break)")
        break  # Exits the loop entirely
    
    print(f"Processing number: {i}")

# 4. Iterating over an Iterable (String)
# Since strings are just sequences of characters, you can loop through them directly.
print("\n--- Looping through a String ---")
word = "JAVA"
for letter in word:
    print(f"Letter: {letter}")