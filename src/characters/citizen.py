import random

from src.characters.base import Human


class Citizen(Human):
    health = 100
    damage = 1
    armor = 1
    agility = 10
    mana = 0
    weapon = 'knuckles'
    alive = True

    def attack(self, another: "Citizen"):
        print(f"{self.name} attack {another.name} by {self.weapon}")
        another.hit(self.damage)

    @staticmethod
    def get_chances(perc: int):
        weights = (1 / 100 * perc, 1 - (1 / 100 * perc))
        return random.choices([True, False], weights=weights, k=1)[0]

    @classmethod
    def hit(cls, damage: int):
        damage = (100 - cls.armor) * (damage / 100)
        cls.health -= damage
        print(f'{cls.__name__} take {damage} damage... Left {cls.health} HP', end='\n\n')
        if cls.health <= 0:
            cls.alive = False
            print(f'{cls.__name__} has gone away...', end='\n\n')
