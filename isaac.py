from fighter import Fighter
from random import randint


class Isaac(Fighter):
    def __init__(self) -> None:
        self.__hp: float = 20
        self.__defense: float = 8
        self.__attack: float = 4
        self.__speed: float = 5

    def get_hp(self) -> float:
        return self.__hp

    def get_attack(self) -> float:
        return self.__attack

    def get_defense(self) -> float:
        return self.__defense

    def get_speed(self) -> float:
        return self.__speed

    def reduce_hp(self, damage: float) -> None:
        self.__hp -= damage

    def compute_damage(self, enemy: Fighter) -> float:
        damage: float = randint(1, self.__attack) - (enemy.get_defense() * 0.1)
        print(damage)
        if damage < 0: 
            return 0
        else: 
            return damage