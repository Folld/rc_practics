from part1.src.characters.citizen import Citizen


class Rogue(Citizen):
    health = 100
    damage = 20
    armor = 15
    agility = 40
    weapon = 'Knife'

    def try_dodge(self):
        return self.get_chances(self.agility)

    def hit(self, damage: int):
        if self.try_dodge():
            print(f'Dodge!', end=' ')
            damage = 0
        return super().hit(damage)
