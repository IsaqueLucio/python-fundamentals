"""
Exercise 3: RPG Characters
File: 12_rpg_characters.py

Rules:
1. Create a parent class 'Character' with __init__ taking 'name' (str), 'hp' (int), and 'attack_power' (int).
2. Create a method 'attack(self)' in Character that prints: "[name] attacks for [attack_power] damage!"
3. Create a child class 'Warrior' inheriting from Character.
4. The Warrior __init__ takes 'name', 'hp', 'attack_power', and 'bonus_damage' (int). Use super().
5. Override 'attack(self)' in Warrior to add 'bonus_damage' to 'attack_power'. 
   Print: "[name] swings a heavy sword for [total_damage] damage!"
6. Create a child class 'Mage' inheriting from Character.
7. The Mage __init__ takes 'name', 'hp', 'attack_power', and 'mana' (int). Use super().
8. Override 'attack(self)' in Mage:
   - If 'mana' >= 10, subtract 10 from mana and print: "[name] casts a fireball for [attack_power * 2] damage! (Mana left: [mana])".
   - If 'mana' < 10, print: "[name] is out of mana and uses a weak staff for [attack_power] damage."
9. Create a Warrior and a Mage object. Test their attack methods (test the Mage twice to see the mana drop!).
"""
from typing import override

class Character:
    
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    
    def attack(self) -> str:
        return f"{self.name} attacks for {self.attack_power} damage!"
    
class Warrior(Character):
    
    def __init__(self, name, hp, attack_power, bonus_damage: int):
        super().__init__(name, hp, attack_power)
        self.bonus_damage = bonus_damage
   
    @override
    def attack(self) -> str:
        total_damage = self.attack_power + self.bonus_damage
        return f"{self.name} swings a heavy sword for {total_damage} damage!"
    
class Mage(Character):
    
    def __init__(self, name, hp, attack_power, mana: int):
        super().__init__(name, hp, attack_power)
        self.mana = mana
   
    @override
    def attack(self) -> str:
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts a fireball for {self.attack_power*2} damage! (Mana left: {self.mana})"
        else:
            return f"{self.name} is out of mana and uses a weak staff for {self.attack_power} damage."

obj1 = Warrior("Conan", 110, 40, 15)
obj2 = Mage("Patolino", 100, 20, 10)
print(obj2.attack())
print(obj1.attack())
print(obj2.attack())
