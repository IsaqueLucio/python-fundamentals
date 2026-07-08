"""
Exercise 2: House Composition
Main File: main.py
Dependencies to create in the same folder: room.py, house.py

--- Rules for 'room.py' ---
1. Create a class 'Room'.
2. The __init__ should take 'name' (str) and 'size_sqm' (float).
3. Create a method 'get_area(self)' that simply returns the 'size_sqm'.

--- Rules for 'house.py' ---
1. Import the 'Room' class.
2. Create a class 'House'.
3. The __init__ should take 'address' (str). Inside it, initialize an empty list called 'rooms'.
4. Create a method 'build_room(self, name: str, size: float)'.
   - STRICT COMPOSITION RULE: This method MUST CREATE the Room object INSIDE its own body, and then append it to the 'rooms' list.
5. Create a method 'get_total_area(self)'. It should loop through all rooms, sum their areas, and return the total sum.

--- Rules for 'main.py' (This file) ---
1. Import the 'House' class (Notice you don't need to import 'Room' here, because the House builds its own rooms!).
2. Create a House object.
3. Call the 'build_room()' method twice (e.g., passing "Kitchen", 15.0 and "Bedroom", 20.0).
4. Print the total area of the house calling 'get_total_area()'.
"""

from house import House

house = House("Midtown Manhattan, New York City, at the intersection of Broadway, Seventh Avenue, and 42nd Street")
house.build_room("Kitchen", 15.0)
house.build_room("Bedroom", 20.0)
print(house.get_total_area())

