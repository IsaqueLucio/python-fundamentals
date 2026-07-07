"""
Python Core - 04 Object-Oriented Programming
File: engine.py
"""

class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is running! Vroom!"