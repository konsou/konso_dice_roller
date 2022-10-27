from dataclasses import dataclass
from typing import Optional


@dataclass
class Roll:
    number_of_dice: int
    dice_sides: int
    bonus: float
    _result: Optional[float] = None

    def roll(self):
        self._result = 0

    @property
    def result(self) -> Optional[float]:
        return self._result

    @property
    def result_as_text(self) -> str:
        return "Result: 0"
