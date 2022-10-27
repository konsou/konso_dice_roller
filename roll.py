from dataclasses import dataclass
from random import randint
from typing import Optional


@dataclass
class Roll:
    number_of_dice: int
    dice_sides: int
    bonus: float
    _result: Optional[float] = None
    _individual_results: Optional[tuple[float, ...]] = None

    def roll(self):
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )
        self._result = 0

    @property
    def result(self) -> Optional[float]:
        return self._result

    @property
    def individual_results(self) -> Optional[tuple[float, ...]]:
        return self._individual_results

    @property
    def result_as_text(self) -> str:
        return f"Result: {self.result}"
