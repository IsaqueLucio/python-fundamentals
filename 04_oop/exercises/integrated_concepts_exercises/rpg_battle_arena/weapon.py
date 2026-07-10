class Weapon:

    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage