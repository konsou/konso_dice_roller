import re

from typing import Literal

from src.roll import Roll


def parse_input(input_string: str) -> Roll:
    input_string = input_string.lower().strip()
    dice, constant = _parse_constant(input_string)
    number_of_dice, dice_sides = dice.split("d")
    return Roll(
        number_of_dice=int(number_of_dice),
        dice_sides=int(dice_sides),
        bonus=constant,
    )


def _parse_constant(input_string: str) -> tuple[str, float]:
    constant_sign = _constant_sign(input_string)
    if not constant_sign:
        return input_string, 0

    split = re.split("[+-]", input_string)
    return split[0], float(f"{constant_sign}{split[1]}")


def _constant_sign(input_string: str) -> Literal["+", "-", ""]:
    if "+" in input_string:
        return "+"
    if "-" in input_string:
        return "-"
    return ""
