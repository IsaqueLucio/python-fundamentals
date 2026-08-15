"""
Python Core - 06 Libraries (numpy)
Exercise 11: The A/B Test Simulator (Intermediate - Logic & Interpretation)
Folder: 11_ab_test_simulator/
Main File: main.py

Rules:
1. Import 'numpy' as 'np'.
2. You have an array representing 20 users who visited a website: users = np.arange(1, 21)
3. Step A (Shuffling):
   - Use 'np.random.shuffle()' to randomize the order of the 'users' array IN-PLACE.
   - Print the shuffled users array.
4. Step B (Splitting):
   - Assign the first 10 users to the 'control_group' array using slicing.
   - Assign the remaining 10 users to the 'treatment_group' array using slicing.
5. Step C (Weighted Choice Simulation):
   - The treatment group received a new layout. Simulate whether each of the 10 users bought a product.
   - Use 'np.random.choice()' to pick from the list [True, False] for the 10 users.
   - Apply a custom probability: 70% chance of True, 30% chance of False (Hint: use the 'p=' parameter).
   - Save the result in 'treatment_purchases' and print it!
"""

import numpy as np

users = np.arange(1, 21)
np.random.shuffle(users)
print(f"Shuffled users array: {users}")
control_group = users[:10]
print(f"Control group:        {control_group}")
treatment_group = users[10:]
print(f"Treatment group:      {treatment_group}")

is_bought = [True, False]
test = np.random.choice(is_bought, size=10, p=[0.7,0.3])
treatment_purchases = []
for user, bought in zip(treatment_group, test):
    temp = {
        "user": user,
        "bought?": bought
    }
    treatment_purchases.append(temp)

print(treatment_purchases)
