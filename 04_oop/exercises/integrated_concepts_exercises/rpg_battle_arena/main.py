"""
Integrated OOP 4: RPG Battle Arena
Main File: main.py
Dependencies to create: weapon.py, character.py, arena.py

--- Rules for 'weapon.py' ---
1. Create 'Weapon' with __init__ taking 'name' (str) and 'damage' (int).
2. Create getter 'get_damage(self)'.

--- Rules for 'character.py' ---
1. Import ABC, abstractmethod, and Weapon.
2. Create 'Character(ABC)'. 
   - __init__ takes 'name' (str), 'hp' (int), 'weapon_name' (str), 'weapon_dmg' (int).
   - Use a protected attribute '_hp' so children can access it.
   - COMPOSITION: Inside __init__, create 'self.weapon = Weapon(weapon_name, weapon_dmg)'.
   - Create abstract method 'attack(self, target)'.
   - Create a method 'take_damage(self, amount)'. Reduce '_hp' by amount.
3. Create 'Hero(Character)'. Override 'attack(target)': target takes damage equal to weapon damage. Print attack message.
4. Create 'Boss(Character)'. Override 'attack(target)': target takes damage equal to weapon damage + 10 (Boss bonus). Print attack message.

--- Rules for 'arena.py' ---
1. Import Character.
2. Create 'Arena'. __init__ takes no arguments.
3. Create 'start_duel(self, fighter1: Character, fighter2: Character)'. (AGGREGATION)
   - Have fighter1 attack fighter2.
   - Have fighter2 attack fighter1.
   - Print the remaining HP of both (you might need to add a get_hp() method in Character!).

--- Rules for 'main.py' (This file) ---
1. Import everything.
2. Create a Hero (e.g., "Arthur", 100 HP, "Excalibur", 20 dmg).
3. Create a Boss (e.g., "Dragon", 200 HP, "Claws", 15 dmg).
4. Create an Arena and start the duel between them!
"""

from character import Hero, Boss
from arena import Arena

hero = Hero("Arthur", 100, "Excalibur", 20)
boss = Boss("Dragon", 200, "Claws", 15)

duel = Arena()
duel.start_duel(hero, boss)