from abc import ABC, abstractmethod
from __future__ import annotations


class Fighter(ABC):
    @abstractmethod
    def get_hp(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_attack(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_defense(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_speed(self) -> float:
        raise NotImplementedError

    @abstractmethod
    def reduce_hp(self, damage: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def compute_damage(self, enemy: Fighter) -> float:
        raise NotImplementedError