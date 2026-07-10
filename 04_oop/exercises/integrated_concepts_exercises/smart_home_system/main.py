"""
Integrated OOP 2: Smart Home System
Main File: main.py
Dependencies to create: device.py, room.py, house.py

--- Rules for 'device.py' ---
1. Create a class 'SmartDevice' with __init__ taking 'name' (str).
2. Set a private attribute '__is_on' to False.
3. Create methods 'turn_on(self)' and 'turn_off(self)' that change the state and print a message (e.g., "[name] is now ON").
4. Create a getter 'is_active(self)' returning the boolean.

--- Rules for 'room.py' ---
1. Import 'SmartDevice'.
2. Create 'Room' with __init__ taking 'name' (str). Initialize an empty list 'devices'.
3. Create 'add_device(self, device: SmartDevice)' that appends the device (AGGREGATION).
4. Create 'turn_on_all(self)' that loops through 'devices' and calls 'turn_on()' on each.

--- Rules for 'house.py' ---
1. Import 'Room'.
2. Create 'House'. __init__ initializes an empty list 'rooms'.
3. Create 'build_room(self, name: str)' that CREATES the Room object inside it and appends it (COMPOSITION).
4. Create 'get_rooms(self)' returning the list of rooms.

--- Rules for 'main.py' (This file) ---
1. Import everything necessary.
2. Create a House. Build a "Living Room" inside it.
3. Get the "Living Room" from the house.
4. Create two SmartDevices independently ("TV" and "Light Bulb").
5. Add the devices to the Living Room.
6. Call 'turn_on_all()' on the Living Room.
"""

from house import House
from device import SmartDevice

house = House()
house.build_room("Living Room")
h = house.get_rooms()[0]

tv = SmartDevice("TV")
light_bulb = SmartDevice("Light")

h.add_device(tv)
h.add_device(light_bulb)
turn_on_all = h.turn_on_all()

print(turn_on_all)
