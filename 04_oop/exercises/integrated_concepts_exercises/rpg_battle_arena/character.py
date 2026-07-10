from abc import ABC, abstractmethod
from typing import override
from weapon import Weapon

class Character(ABC):

    def __init__(self, name: str, hp: int, weapon_name: str, weapon_damage: int):
        self.weapon = Weapon(weapon_name, weapon_damage)
        self.name = name
        self._hp = hp
        
    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, amount):
        self._hp -= amount
        return self._hp
    
    def get_hp(self):
        return self._hp
    
    def get_name(self):
        return self.name
    
class Hero(Character):

    @override
    def attack(self, target) -> str:
        damage = self.weapon.get_damage()
        target.take_damage(damage)
        return f"The hero {self.name} attack the character {target.get_name()} and causes {self.weapon.get_damage()} damage to his HP."
    
class Boss(Character):

    @override
    def attack(self, target) -> str:
        damage = self.weapon.get_damage() + 10
        target.take_damage(damage)
        return f"The Boss {self.name} attack the character {target.get_name()} and causes {self.weapon.get_damage()} damage to his HP."