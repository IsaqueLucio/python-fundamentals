"""
Integrated OOP 1: Zoo Management System
Main File: main.py
Dependencies to create: animal.py, enclosures.py

--- Rules for 'animal.py' ---
1. Import ABC and abstractmethod.
2. Create an abstract class 'Animal(ABC)'.
   - __init__ takes 'name' (str) and sets a protected attribute '_hunger' to 100.
   - Create a getter 'get_hunger(self)' returning the hunger level.
   - Create an abstract method 'feed(self) -> str'.
3. Create a child class 'Lion(Animal)'.
   - Override 'feed'. It should decrease '_hunger' by 40.
   - Return: "[name] the Lion eats a big chunk of meat. Hunger is now [_hunger]."
4. Create a child class 'Monkey(Animal)'.
   - Override 'feed'. It should decrease '_hunger' by 20.
   - Return: "[name] the Monkey eats a banana. Hunger is now [_hunger]."

--- Rules for 'enclosures.py' ---
1. Import the 'Animal' class.
2. Create a class 'Enclosure'.
   - __init__ takes 'name' (str) (e.g., "Savanna" or "Jungle"). Initialize an empty list 'animals'.
3. Create a method 'add_animal(self, animal: Animal)'.
   - Append the animal to the 'animals' list (AGGREGATION).
   - Print: "[animal.name] was added to the [name] enclosure."
4. Create a method 'feed_all(self)'.
   - Iterate over the 'animals' list.
   - Call the 'feed()' method on each animal and print the returned string (POLYMORPHISM).

--- Rules for 'main.py' (This file) ---
1. Import Lion, Monkey, and Enclosure.
2. Create an Enclosure object (e.g., "African Safari").
3. Create one Lion and two Monkeys independently.
4. Add the animals to the enclosure using 'add_animal()'.
5. Call 'feed_all()' on the enclosure object to see the polymorphism in action!
"""

from animal import Lion, Monkey
from enclosures import Enclosures

enclosure = Enclosures("African Safari")

lion = Lion("Simba", "Panthera leo")
monkey_01 = Monkey("Tarzan", "Gorilla gorilla gorilla")
monkey_02 = Monkey("Cesar", "Chimpanzé")

print(enclosure.add_animal(lion))
print(enclosure.add_animal(monkey_01))
print(enclosure.add_animal(monkey_02))

print(enclosure.feed_all())
