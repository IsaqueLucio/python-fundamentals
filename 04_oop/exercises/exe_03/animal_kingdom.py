"""
Exercise 1: Animal Kingdom
File: 10_animal_kingdom.py

Rules:
1. Create a parent class called 'Animal'.
2. The __init__ takes 'name' (str) and 'species' (str).
3. Create a method 'make_sound(self)' in the Animal class that returns: "[name] makes a generic sound."
4. Create a child class called 'Dog' that inherits from Animal.
5. In the Dog class, override the 'make_sound(self)' method to return: "[name] says: Woof! Woof!"
6. Create another child class called 'Cat' that inherits from Animal.
7. In the Cat class, override the 'make_sound(self)' method to return: "[name] says: Meow!"
8. Create one Dog object and one Cat object. (Notice you don't need to write an __init__ for them, they use the parent's!).
9. Print the result of make_sound() for both objects.
"""
from typing import override

class Animal:

    def __init__(self, name: str, species: str):
        self.name = name
        self.species =  species

    def make_sound(self) -> str:
        return f"{self.name} makes a generic sound."
    
class Dog(Animal):

    def __init__(self, name: str, species: str):
        super().__init__(name, species)
    
    @override
    def make_sound(self) -> str:
        return f"{self.name} says: Woof! Woof!"

class Cat(Animal):

    def __init__(self, name: str, sprecies: str):
        super().__init__(name, sprecies)
    
    @override
    def make_sound(self) -> str:
        return f"{self.name} says: Meow!"

dog = Dog("Rex","Bulldog")
cat = Cat("Garfield", "Persa")
print(dog.make_sound())
print(cat.make_sound())