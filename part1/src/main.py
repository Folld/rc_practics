import random
import time

from part1.src.characters import Citizen, Mage, Rogue, Priest, Warrior

if __name__ == '__main__':
    team = [Priest, Citizen, Mage, Rogue, Warrior]

    battlefield = [character() for character in team]

    while len(battlefield) > 1:
        character = random.choice(battlefield)
        enemy = random.choice(list(filter(lambda x: x is not character, battlefield)))
        character.attack(enemy)
        if not enemy.alive:
            battlefield = list(filter(lambda x: x is not enemy, battlefield))
        time.sleep(1)

    print(f'Winner - {battlefield.pop()}')

