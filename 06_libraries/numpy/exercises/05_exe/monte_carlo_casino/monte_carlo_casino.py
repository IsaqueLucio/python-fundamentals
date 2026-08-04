"""
Python Core - 06 Libraries (numpy)
Exercise 12: The Monte Carlo Casino (Hard - Problem Solving & Random Walks)
Folder: 12_monte_carlo_casino/
Main File: main.py

Scenario:
You are simulating a gambler's night at the casino using the Monte Carlo method. 
The gambler starts with a specific bankroll and places 100 consecutive bets on Roulette (betting on Red).

Rules:
1. Import 'numpy' as 'np'.
2. Setup the simulation:
   - Set the seed to 777.
   - initial_balance = 1000
   - bet_size = 50
3. Step A (The Outcomes):
   - In Roulette, betting on Red yields a win exactly 18 out of 38 times.
   - Create an array of possible outcomes per bet: [bet_size, -bet_size] (Win $50 or Lose $50).
   - Calculate the exact probabilities for winning and losing as floats: win_prob = 18/38, loss_prob = 20/38.
4. Step B (The Simulation):
   - Use 'np.random.choice()' to simulate 100 consecutive bets. Pass your outcomes array, set size=100, and use the 'p=' parameter to pass your calculated probabilities [win_prob, loss_prob].
   - Save the generated array as 'gambler_night'.
5. Step C (Aggregation):
   - Use 'np.sum()' on the 'gambler_night' array to calculate the net profit (or loss) for the entire night.
   - Add this net result to the 'initial_balance' to find the 'final_balance'.
   - Print the Net Profit/Loss and the Final Balance!
"""

import numpy as np

np.random.seed(777)

initial_balance = 1000
bet_size = 50
outcomes = [bet_size, -bet_size]
win_prob = 18/38
loss_prob = 20/38
gambler_night = np.random.choice(outcomes, size=100, p=[win_prob, loss_prob])
gnrs = []
for i in gambler_night:
   if i > 0:
      temp = {"result": "WIN", "amount": i}
      gnrs.append(temp)
   else:
      temp = {"result": "LOSS", "amount": i}
      gnrs.append(temp)
for i,play in enumerate(gnrs):
   print(f"{i+1}° play:\n{play}")

tgn = np.sum(gambler_night)
final_balance = initial_balance + tgn
if final_balance > initial_balance:
   print(f"Congratulations, you made a profit of: ${tgn}\n"
         f"So its final balance was then of: ${final_balance}")
elif final_balance < initial_balance:
   print(f"Unfortunately, you were unlucky and lost the amount of: ${tgn}\n"
         f"So its final balance was then of: ${final_balance}")
else:
   print("Surprisingly, you neither won nor lost anything.\n"
         f"So its final balance was then of: ${final_balance}")