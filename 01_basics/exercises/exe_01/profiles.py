"""
Create four variables to represent an RPG character:
name (text), rpg_class (text), level (integer), health (decimal), and has_magic (boolean).
Print the values and use the type() function on each to confirm their types.
"""

# 1. Creating the variables
name = "Aaron"
rpg_class = "Warrior"
level = 172
health = 96.8
has_magic = False

#2. Printing the values of the profile and their types
print(f"Character name: ",name,"| Variable type: ",type(name))
print(f"Character class: ",rpg_class,"| Variable type: ",type(rpg_class))
print(f"Character level: ",level,"| Variable type: ",type(level))
print(f"Character health: ",health,"| Variable type: ",type(health))
print(f"Character has magic: ",has_magic,"| Variable type: ",type(has_magic))