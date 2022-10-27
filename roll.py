from typing import NamedTuple


class Roll(NamedTuple):
    number_of_dice: int
    dice_sides: int
    bonus: float
