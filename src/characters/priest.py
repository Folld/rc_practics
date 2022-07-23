from src.characters.citizen import Citizen


class Priest(Citizen):
    health = 150
    damage = 10
    armor = 25
    weapon = 'hummer'
    mana = 100

    @classmethod
    def heal(cls):
        price = 20
        if cls.mana >= price:
            cls.health += price
            cls.mana -= price
            print(f'{cls.__name__} heal! HP = {cls.health}')

    def hit(self, damage: int):
        if self.get_chances(25):
            self.heal()
        return super().hit(damage)

