from random import randint
from typing import Optional


class Roll:
    def __init__(self, number_of_dice: int, dice_sides: int, bonus: float) -> None:
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        self._individual_results: Optional[tuple[float, ...]] = None

        self.roll()

    def roll(self):
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )

    @property
    def result(self) -> Optional[float]:
        return (
            sum(self.individual_results)
            if self.individual_results is not None
            else None
        )

    @property
    def individual_results(self) -> Optional[tuple[float, ...]]:
        return self._individual_results

    @property
    def result_as_text(self) -> str:
        return f"Result: {self.result}"
