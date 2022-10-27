import re

from typing import Literal

from src.roll import Roll


def parse_input(input_string: str) -> Roll:
    input_string = input_string.lower().strip()
    dice, bonus = _parse_bonus(input_string)
    number_of_dice, dice_sides = dice.split("d")
    return Roll(
        number_of_dice=int(number_of_dice),
        dice_sides=int(dice_sides),
        bonus=bonus,
    )


def _parse_bonus(input_string: str) -> tuple[str, float]:
    """Return (dice part, bonus)
    e.g. ("5d6", 2), ("3d10", -3)"""
    sign = _sign_in_string(input_string)
    if not sign:
        return input_string, 0

    split = re.split("[+-]", input_string)
    return split[0], float(f"{sign}{split[1]}")


def _sign_in_string(input_string: str) -> Literal["+", "-", ""]:
    if "+" in input_string:
        return "+"
    if "-" in input_string:
        return "-"
    return ""
