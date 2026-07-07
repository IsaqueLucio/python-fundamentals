"""
Python Core - 04 Object-Oriented Programming
File: 14_polymorphism.py
Description: Polymorphism and Duck Typing in action.
"""

print("--- 1. Creating Unrelated Classes ---")

# These classes do NOT inherit from a common parent. 
# They are completely independent, but they share a method name: 'deliver()'.

class Drone:
    def deliver(self):
        return "Flying over traffic to deliver the package."

class Truck:
    def deliver(self):
        return "Driving on the highway to deliver the cargo."

class Bicycle:
    def deliver(self):
        return "Pedaling through the bike lane to deliver the food."


print("\n--- 2. The Power of Polymorphism ---")

# This function expects ANY object, as long as it knows how to "deliver".
def process_delivery(vehicle):
    # The function doesn't care if it's a Drone, Truck, or Bicycle.
    # It just calls the method and lets the object figure out the rest.
    print(vehicle.deliver())

# Let's test it!
my_drone = Drone()
my_truck = Truck()

process_delivery(my_drone)
process_delivery(my_truck)


print("\n--- 3. Polymorphism in Loops ---")

# This is how you will use it 90% of the time in the real world:
fleet = [Drone(), Truck(), Bicycle(), Drone()]

print("Dispatching the entire fleet:")
for vehicle in fleet:
    # We call the exact same method on different objects.
    # Each object reacts in its own specific way!
    print(f" -> {vehicle.deliver()}")