from part1.src.characters.citizen import Citizen


class Priest(Citizen):
    health = 150
    damage = 10
    armor = 25
    weapon = 'hummer'
    mana = 100

    def heal(self):
        price = 20
        if self.mana >= price:
            self.health += price
            self.mana -= price
            print(f'{self.name} heal! HP = {self.health}')

    def hit(self, damage: int):
        if self.get_chances(25):
            self.heal()
        return super().hit(damage)

