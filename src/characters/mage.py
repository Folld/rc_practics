import random

from src.characters.citizen import Citizen


class Mage(Citizen):
    health = 75
    damage = 50
    armor = 10
    mana = 200

    def __init__(self):
        super().__init__()
        self.__magic_spells = ['ice_pick', 'fireball', 'lightning_strike']

    def attack(self, another: "Citizen"):
        spell = getattr(self, random.choice(self.__magic_spells))
        print(f'{self.name} attack {another.name} by {spell.__func__.__name__}')
        return spell(another)

    def cast_magic(self, another: "Citizen", price=0):
        damage = self.damage
        if self.mana >= price:
            self.mana -= price
            damage = round(self.damage + price)
        return another.hit(damage)

    def fireball(self, another: "Citizen"):
        price = 15
        return self.cast_magic(another, price)

    def ice_pick(self, another: "Citizen"):
        price = 25
        return self.cast_magic(another, price)

    def lightning_strike(self, another: "Citizen"):
        price = 50
        return self.cast_magic(another, price)
