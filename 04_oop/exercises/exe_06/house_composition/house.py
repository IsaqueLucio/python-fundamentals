from room import Room

class House:

    def __init__(self, address: str):
        self.adress = address
        self.rooms = []

    def build_room(self, name: str, size: float):
        new_room = Room(name, size)
        self.rooms.append(new_room)

    def get_total_area(self):
        sum = 0
        for room in self.rooms:
            house_room = room.get_area() 
            sum += house_room
        return sum