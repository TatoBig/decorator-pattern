from fighter_decorator import FighterDecorator
from fighter import Fighter


class BrimstoneDecorator(FighterDecorator):
    def __init__(self, fighter: Fighter) -> None:
        super().__init__(fighter)

    def compute_damage(self, enemy: Fighter) -> float:
        return super().compute_damage(enemy) * 2
        