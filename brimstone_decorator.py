from fighter_decorator import FighterDecorator
from fighter import Fighter


class BrimstoneDecorator(FighterDecorator):
    def __init__(self, fighter: Fighter) -> None:
        super().__init__(fighter)

    def compute_damage(self, enemy: Fighter) -> float:
        damage: float = (self.get_fighter().get_attack * 2) - (enemy.get_defense() * 0.1)
        if damage < 0: 
            return 0
        else: 
            return damage