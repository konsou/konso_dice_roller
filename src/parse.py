import re

from typing import Literal

from src.format import roll_as_text, roll_as_markdown_text
from src.roll import Roll, RollInfo


def parse_input(input_string: str) -> RollInfo:
    input_string = input_string.lower()
    # Strip all whitespace
    input_string = re.sub(r"\s+", "", input_string)

    try:
        dice, bonus = _parse_bonus(input_string)
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    try:
        number_of_dice_text, dice_sides_text = dice.split("d")
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    try:
        number_of_dice = int(number_of_dice_text)
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    try:
        dice_sides = int(dice_sides_text)
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    if dice_sides < 1:
        raise ValueError("Virhe syötteen käsittelyssä")

    return RollInfo(
        number_of_dice=number_of_dice,
        dice_sides=dice_sides,
        bonus=bonus,
    )


def roll_string_from_input(input_string: str) -> str:
    roll_info = parse_input(input_string)
    roll = Roll.from_roll_info(roll_info)
    return roll_as_text(roll)


def markdown_roll_string_from_input(input_string: str) -> str:
    roll_info = parse_input(input_string)
    roll = Roll.from_roll_info(roll_info)
    return roll_as_markdown_text(roll)


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
