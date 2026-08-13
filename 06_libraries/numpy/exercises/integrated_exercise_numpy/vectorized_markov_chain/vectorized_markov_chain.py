"""
Python Core - 06 Libraries (numpy)
Exercise 16: The Vectorized Markov Chain (Hardcore - Linear Algebra & Transition States)
Folder: 16_vectorized_markov_chain/
Main File: main.py

Scenario:
You are analyzing user journeys in an e-commerce app. There are 4 states: [Home, Product, Cart, Checkout]. You have a transition matrix detailing the probability of moving from one state to another in the next click. 

Rules:
1. Import 'numpy' as 'np'.
2. Step A (The Matrices):
   - Create a 1D array representing 10,000 users starting exactly at the "Home" state:
     current_state = np.array([10000, 0, 0, 0])
   - Create the 4x4 transition matrix (Rows sum to 1):
     T = np.array([
         [0.2, 0.6, 0.2, 0.0],  # From Home
         [0.1, 0.4, 0.4, 0.1],  # From Product
         [0.3, 0.2, 0.3, 0.2],  # From Cart
         [0.0, 0.0, 0.0, 1.0]   # From Checkout (Once checked out, they stay checked out)
     ])
3. Step B (The Simulation via Linear Algebra):
   - A Markov Chain progresses by multiplying the current state vector by the transition matrix.
   - Use the Dot Product operator '@' to update 'current_state' 15 times (simulating 15 clicks per user).
   - Yes, you can use a small 'for _ in range(15):' loop for the time steps, but the calculation inside MUST be purely vectorized: current_state = current_state @ T
4. Step C (Matrix Power Projection):
   - To jump 100 steps into the future instantly without a loop, we can raise the transition matrix to the power of 100.
   - Use 'np.linalg.matrix_power(T, 100)' to create 'T_100'.
   - Multiply the original starting vector [10000, 0, 0, 0] by 'T_100'.
5. Validate:
   - Both methods (looping 15 times vs matrix power 100) should show that almost all users eventually get absorbed into the "Checkout" state. Print the resulting user distributions for both approaches!
"""
#1
import numpy as np
#2
original_current_state = np.array([10000, 0, 0, 0])
current_state = original_current_state.copy()
T = np.array([
   [0.2, 0.6, 0.2, 0.0],
   [0.1, 0.4, 0.4, 0.1],
   [0.3, 0.2, 0.3, 0.2],
   [0.0, 0.0, 0.0, 1.0]
   ])
#3
for _ in range(15):
    current_state = current_state @ T
#4
T_100 = np.linalg.matrix_power(T, 100)
final = original_current_state @ T_100

print("After 15 clicks (loop):")
print(f"  Home:      {current_state[0]:.2f}")
print(f"  Product:   {current_state[1]:.2f}")
print(f"  Cart:      {current_state[2]:.2f}")
print(f"  Checkout:  {current_state[3]:.2f}")
print("\nAfter 100 clicks (matrix power):")
print(f"  Home:      {final[0]}")
print(f"  Product:   {final[1]}")
print(f"  Cart:      {final[2]}")
print(f"  Checkout:  {final[3]}")