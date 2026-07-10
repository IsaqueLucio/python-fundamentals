from room import Room

class House:

    def __init__(self):
        self.rooms = []
    
    def build_room(self, name: str):
        new_room = Room(name)
        self.rooms.append(new_room)
    
    def get_rooms(self):
        return self.rooms