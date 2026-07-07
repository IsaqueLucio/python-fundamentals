"""
Python Core - 04 Object-Oriented Programming
File: 15_relationships.py
Description: Aggregation vs. Composition with Modular Imports.
"""

# Importing the classes from the other files
from engine import Engine
from player import Player

print("--- 1. COMPOSITION (Strong Relationship) ---")
class Car:
    def __init__(self, brand: str, horsepower: int):
        self.brand = brand
        # COMPOSITION: The Car creates the Engine INSIDE its own constructor.
        # If this Car object is destroyed, its Engine is destroyed with it.
        self.engine = Engine(horsepower)

    def drive(self):
        # The Car delegates the action to its internal Engine object
        print(f"[{self.brand}] {self.engine.start()}")

my_car = Car("Porsche", 450)
my_car.drive()


print("\n--- 2. AGGREGATION (Weak Relationship) ---")
class Team:
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.players = [] # Starts empty

    # AGGREGATION: The Team receives a Player object from the OUTSIDE.
    def add_player(self, new_player: Player):
        self.players.append(new_player)
        print(f"{new_player.name} joined {self.team_name}!")

    def show_roster(self):
        print(f"--- {self.team_name} Roster ---")
        for p in self.players:
            print(p.get_info())

# The Players are created OUTSIDE the Team. They have their own independent lives.
p1 = Player("Lionel", "Forward")
p2 = Player("Virgil", "Defender")

my_team = Team("FC Python")

# We aggregate them into the team
my_team.add_player(p1)
my_team.add_player(p2)

my_team.show_roster()