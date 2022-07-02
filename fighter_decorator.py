from fighter import Fighter
from random import randint

class FighterDecorator(Fighter):
    def __init__(self, fighter: Fighter) -> None:
        self.__decorated_fighter: Fighter = fighter

    def get_hp(self) -> float:
        return self.__decorated_fighter.get_hp()

    def get_attack(self) -> float:
        return self.__decorated_fighter.get_attack()

    def get_defense(self) -> float:
        return self.__decorated_fighter.get_defense()

    def get_speed(self) -> float:
        return self.__decorated_fighter.get_speed()

    def get_fighter(self) -> Fighter:
        return self.__decorated_fighter

    def reduce_hp(self, damage: float) -> None:
        return self.__decorated_fighter.reduce_hp(damage)

    def compute_damage(self, enemy: Fighter) -> float:
        damage: float = randint(1, self.__decorated_fighter.get_attack()) - (enemy.get_defense() * 0.1)
        if damage < 0: 
            return 0
        else: 
            return damage