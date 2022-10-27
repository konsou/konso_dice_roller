from random import randint
from typing import NamedTuple


class RollInfo(NamedTuple):
    number_of_dice: int
    dice_sides: int
    bonus: float = 0


class Roll:
    def __init__(self, number_of_dice: int, dice_sides: int, bonus: float) -> None:
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        self._individual_results: tuple[int, ...] = ()

        self._roll()

    @classmethod
    def from_roll_info(cls, roll_info: RollInfo) -> "Roll":
        return cls(
            number_of_dice=roll_info.number_of_dice,
            dice_sides=roll_info.dice_sides,
            bonus=roll_info.bonus,
        )

    def _roll(self):
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )

    @property
    def result(self) -> float:
        return sum(self.individual_results) + self.bonus

    @property
    def individual_results(self) -> tuple[float, ...]:
        return self._individual_results
