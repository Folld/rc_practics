from src.characters.citizen import Citizen


class Warrior(Citizen):
    health = 180
    damage = 10
    armor = 25
    weapon = 'Sword'

    def try_block(self):
        return self.get_chances(25)

    def hit(self, damage: int):
        if self.try_block():
            print(f'Block by shield! No damage.', end=' ')
            damage = 0
        return super().hit(damage)
