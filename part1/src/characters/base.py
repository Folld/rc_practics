from abc import ABC, abstractmethod


class Human(ABC):
    health: float = None
    damage: int = None
    armor: int = None
    agility: int = None
    mana: int = None
    weapon: str = None

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__class__.__name__

    @abstractmethod
    def attack(self, another: "Human"):
        raise NotImplemented()

    @abstractmethod
    def hit(self, damage: int):
        raise NotImplemented()
