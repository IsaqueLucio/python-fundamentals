"""
Exercise 1: Smart Thermostat
File: 06_smart_thermostat.py

Rules:
1. Create a class called 'Thermostat'.
2. The __init__ method should set a private attribute '__temperature' to 20 (default value).
3. Create a getter method called 'get_temperature(self)' that returns the current '__temperature'.
4. Create a setter method called 'set_temperature(self, temp)'.
   - Add validation: The temperature can only be set between 10 and 30 degrees.
   - If the 'temp' is valid, update '__temperature' and print a success message.
   - If it's invalid, DO NOT update, and print an error message.
5. Create a Thermostat object.
6. Try to set the temperature to 35 (should fail).
7. Try to set the temperature to 22 (should succeed).
8. Print the current temperature using the getter method.
"""

class Thermostat:

    def __init__(self):
        self.__temperature = 20
    
    def get_temperature(self) -> float:
        return self.__temperature
    
    def set_temperature(self, temp: float):
        if 10 <= temp <= 30:
            self.__temperature = temp
            print(f"Done! The current temperature is {temp}C°.")
        else: 
            print("ERROR: The temperature can only be set between 10 and 30 degrees.")

obj = Thermostat()
print(f"Current temperature {obj.get_temperature()}C°.")
obj.set_temperature(35.0)
obj.set_temperature(22.0)
print(f"Current temperature {obj.get_temperature()}C°.")