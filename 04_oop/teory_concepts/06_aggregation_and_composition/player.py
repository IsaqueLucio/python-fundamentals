"""
Python Core - 04 Object-Oriented Programming
File: player.py
"""

class Player:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} ({self.position})"