from fighter import Fighter


class Judas(Fighter):
    def __init__(self) -> None:
        self.__hp: float = 10
        self.__defense: float = 0
        self.__attack: float = 10
        self.__speed: float = 6

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
        damage: float = self.__attack - (enemy.get_defense() * 0.1)
        if damage < 0: 
            return 0
        else: 
            return damage