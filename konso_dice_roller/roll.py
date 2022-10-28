from enum import Enum
from random import randint
from typing import NamedTuple

from .math import (
    greater_than_or_equal,
    less_than_or_equal,
    greater_than,
    less_than,
    equal,
)


class ResultModes(Enum):
    ADDITION = 0
    COUNT_SUCCESSES = 1


class RollInfo(NamedTuple):
    number_of_dice: int
    dice_sides: int
    bonus: float = 0
    result_mode: ResultModes = ResultModes.ADDITION
    comparison_operator: str = ""
    comparison_value: float = 0


COMPARISON_FUNCTIONS = {
    ">=": greater_than_or_equal,
    "<=": less_than_or_equal,
    ">": greater_than,
    "<": less_than,
    "=": equal,
}


class Roll:
    def __init__(
        self,
        number_of_dice: int,
        dice_sides: int,
        bonus: float,
        result_mode: ResultModes = ResultModes.ADDITION,
        comparison_operator: str = "",
        comparison_value: float = 0,
    ) -> None:
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        self.result_mode = result_mode
        self.comparison_operator = comparison_operator
        self.comparison_value = comparison_value
        self._individual_results: tuple[int, ...] = ()

        self._roll()

    @classmethod
    def from_roll_info(cls, roll_info: RollInfo) -> "Roll":
        return cls(
            number_of_dice=roll_info.number_of_dice,
            dice_sides=roll_info.dice_sides,
            bonus=roll_info.bonus,
        )

    def _roll(self) -> None:
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )

    @property
    def result(self) -> float:
        if self.result_mode == ResultModes.ADDITION:
            return sum(self.individual_results) + self.bonus
        if self.result_mode == ResultModes.COUNT_SUCCESSES:
            comparison_function = COMPARISON_FUNCTIONS[self.comparison_operator]
            # This is a hacky line that exploits that True == 1. Sue me :P
            return sum(
                (
                    comparison_function(r, self.comparison_value)
                    for r in self.individual_results
                )
            )
        raise NotImplementedError(
            f"Result mode {self.result_mode.name} not implemented"
        )

    @property
    def individual_results(self) -> tuple[float, ...]:
        return self._individual_results
