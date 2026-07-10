from abc import ABC, abstractmethod
from typing import override

class Animal(ABC):

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self._hunger = 100

    def get_hunger(self) -> int:
        return self._hunger
    
    @abstractmethod
    def feed(self) -> str:
        pass

class Lion(Animal):

    def __init__(self, name, species):
        super().__init__(name, species)
    
    @override
    def feed(self) -> str:
        self._hunger -= 40
        return f"{self.name} the Lion eats a big chunk of meat. Hunger is now {self.get_hunger()}.\n"
    
class Monkey(Animal):

    def __init__(self, name, species):
        super().__init__(name, species)

    @override
    def feed(self) -> str:
        self._hunger -= 20
        return f"{self.name} the Monkey eats a banana. Hunger is now {self.get_hunger()}.\n"