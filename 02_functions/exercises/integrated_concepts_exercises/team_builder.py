"""
Challenge 3: Dynamic Team Builder
File: 12_team_builder.py

Rules:
1. Create a function called 'build_team' that takes 'team_name' as a standard parameter and '**players' for dynamic player-score pairs.
2. Inside the function, print "--- Team: [team_name] Leaderboard ---".
3. The '**players' kwargs creates a dictionary. Convert its items into a list of tuples using:
   player_list = list(players.items())
   (This will look like: [("Isaque", 95), ("Alice", 88)])
4. Use the .sort() method with a lambda function to sort 'player_list' by their score (the second item in the tuple).
5. Remember to use 'reverse=True' to sort from highest to lowest score.
6. Loop through the sorted list and print each player and their score.
7. Call the function: build_team("Python Ninjas", isaque=95, alice=88, bob=92, charlie=70)
"""

def build_team(team_name, **players):
    players_list = list(players.items())
    players_list.sort(key=lambda score: score[1], reverse=True)
    print(f"--- Team: {team_name} Leaderboard ---")
    for key, value in players_list:
        print(f"Player: {key} | Score: {value}")

build_team("Python Ninjas", isaque=95, alice=88, bob=92, charlie=70)