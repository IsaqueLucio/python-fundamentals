"""
Exercise 3: Leaderboard Slicing
File: 03_leaderboard_slicing.py

Rules:
1. Create a list called 'scores' with 7 numbers, ordered from highest to lowest.
   Example: [1000, 950, 820, 740, 600, 510, 400]
2. The front-end only wants to show the Top 3 players. Use slicing to get the first 3 elements and print them.
   Print: f"Top 3: {scores[...]}"
3. The front-end now wants the "middle" players. Use slicing to get the scores from index 2 up to index 5 (exclusive) and print them.
4. Use slicing to get all players from index 4 to the end of the list and print them.
"""

# 1. Create a list called 'scores' with 7 numbers, ordered from highest to lowest.
scores = [1000, 950, 820, 740, 600, 510, 400]
print("\n--- Score of The Players ---\n")
for i in range(7):
    print(f"Score player Top {i+1}°: {scores[i]}")

# 2. The front-end only wants to show the Top 3 players. Use slicing to get the first 3 elements and print them.
print("\n--- Top 3 Scores ---\n")
top3 = scores[:3]
for i in range(3):
    print(f"Score Top {i+1}°: {top3[i]}")

# 3. The front-end now wants the "middle" players. Use slicing to get the scores from index 2 up to index 5 (exclusive) and print them.
print("\n--- Middle Scores ---\n")
midleScores = scores[2:5]
for i in range(3):
    print(f"Midles socres: {midleScores[i]}")

# 4. Use slicing to get all players from index 4 to the end of the list and print them.
print("\n--- Lats Scores ---\n")
lastScores = scores[4:]
for i in range(3):
    print(f"Last socres: {lastScores[i]}")