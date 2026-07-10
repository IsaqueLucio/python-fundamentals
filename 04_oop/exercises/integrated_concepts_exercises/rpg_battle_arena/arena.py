from character import Character

class Arena:

    def start_duel(self, fighter_01: Character, fighter_02: Character):
        print(fighter_01.attack(fighter_02))
        print(fighter_02.attack(fighter_01))
        print(f"{fighter_01.get_name()} remaining HP: {fighter_01.get_hp()}\n{fighter_02.get_name()} remaining HP: {fighter_02.get_hp()}")
