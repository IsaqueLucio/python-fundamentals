class Room:

    def __init__(self, name: str, size_sqm: float):
        self.name = name
        self.size_sqm = size_sqm

    def get_area(self) -> float:
        return self.size_sqm