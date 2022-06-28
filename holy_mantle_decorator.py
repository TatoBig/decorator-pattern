from fighter_decorator import FighterDecorator
from fighter import Fighter


class HolyMantleDecorator(FighterDecorator):
    def __init__(self, fighter: Fighter) -> None:
        super().__init__(fighter)
        self.__uses: int = 1

    def reduce_hp(self, damage: float) -> None:
        if self.__uses != 0:
            self.__uses -= 1
        else: 
            self.__decorated_fighter.reduce_hp(damage)