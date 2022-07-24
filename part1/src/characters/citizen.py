import random

from part1.src.characters.base import Human


class Citizen(Human):
    health = 100
    damage = 5
    armor = 5
    agility = 10
    mana = 0
    weapon = 'knuckles'

    def __init__(self):
        self.__alive = True

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value: bool):
        if self.__alive and not value:
            self.__alive = value
            print(f'{self.name} has gone away...', end='\n\n')

    def attack(self, another: "Citizen"):
        print(f"{self.name} attack {another.name} by {self.weapon}")
        another.hit(self.damage)

    @staticmethod
    def get_chances(perc: int):
        weights = (1 / 100 * perc, 1 - (1 / 100 * perc))
        return random.choices([True, False], weights=weights, k=1)[0]

    def hit(self, damage: int):
        damage = (100 - self.armor) * (damage / 100)
        self.health -= damage
        print(f'{self.name} take {damage} damage... Left {self.health} HP', end='\n\n')
        if self.health <= 0:
            self.alive = False
