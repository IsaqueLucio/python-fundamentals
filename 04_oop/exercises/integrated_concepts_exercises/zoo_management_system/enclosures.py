from animal import Animal

class Enclosures:

    def __init__(self, name: str):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal: Animal) -> str:
        self.animals.append(animal)
        return f"{animal.name} was added to the {self.name} enclosure.\n"
    
    def feed_all(self) -> str:
        animals = []
        for animal in self.animals:
            animals.append(animal.feed())
        return "\n".join(animals)    
        
            
    
