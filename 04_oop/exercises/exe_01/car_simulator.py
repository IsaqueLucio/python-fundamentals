"""
Exercise 2: Car Simulator
File: 03_car_simulator.py

Rules:
1. Create a class called 'Car'.
2. The __init__ method should take 'brand' and 'model'.
3. Create an attribute called 'speed' and set it to 0 initially.
4. Create a method called 'accelerate(self, amount)'. It should add 'amount' to 'self.speed' and print the new speed.
5. Create a method called 'brake(self, amount)'. It should subtract 'amount' from 'self.speed'. 
   - Add an 'if' statement: if the speed drops below 0, force it back to 0 (a car can't have negative speed).
   - Print the new speed.
6. Create a Car object.
7. Accelerate it by 50, then accelerate by 30.
8. Brake by 100. The final speed should print as 0, not -20.
"""

class Car:

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, amount: int):
        self.speed += amount
        print(f"Accelerating! The current speed is {self.speed}Km/h.")
    
    def brake(self, amount: int):
        self.speed -= amount
        if  self.speed < 0:
            self.speed = 0
        print(f"Braking! The current speed is {self.speed}Km/h.")
    
car = Car("Hyundai", "Azera")

car.accelerate(50)
car.accelerate(30)
car.brake(100)