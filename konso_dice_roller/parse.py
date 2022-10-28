import re

from typing import Literal

from .roll import ResultModes, RollInfo


def parse_input(input_string: str) -> RollInfo:
    input_string = input_string.lower()
    # Strip all whitespace
    input_string = re.sub(r"\s+", "", input_string)

    operator = get_comparison_operator(input_string)
    if operator:
        try:
            input_string, after_operator = input_string.split(operator)
        except ValueError:
            raise ValueError("Virhe syötteen käsittelyssä")
        try:
            after_operator_number = float(after_operator)
        except ValueError:
            raise ValueError("Virhe syötteen käsittelyssä")
    else:
        after_operator_number = 0

    result_mode = ResultModes.ADDITION if not operator else ResultModes.COUNT_SUCCESSES

    try:
        dice, bonus = _parse_bonus(input_string)
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    try:
        number_of_dice_text, dice_sides_text = dice.split("d")
    except ValueError:
        raise ValueError("Virhe syötteen käsittelyssä")

    if not number_of_dice_text:
        number_of_dice = 1
    else:
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
        result_mode=result_mode,
        comparison_operator=operator,
        comparison_value=after_operator_number,
    )


def validate_roll_info(
    roll_info: RollInfo,
    number_of_dice_limit: int = 0,
    dice_sides_limit: int = 0,
    bonus_absolute_value_limit: int = 0,
) -> None:
    """Raise ValueErrors if values are higher than the limit"""
    if number_of_dice_limit and roll_info.number_of_dice > number_of_dice_limit:
        raise ValueError("Liian monta noppaa")
    if dice_sides_limit and roll_info.dice_sides > dice_sides_limit:
        raise ValueError("Nopilla liian monta sivua")
    if bonus_absolute_value_limit:
        if roll_info.bonus > bonus_absolute_value_limit:
            raise ValueError("Bonus liian suuri")
        if roll_info.bonus < -bonus_absolute_value_limit:
            raise ValueError("Bonus liian pieni")


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


def get_comparison_operator(
    input_string: str,
) -> Literal[">=", "<=", ">", "<", "=", ""]:
    match = re.search("(>=|<=|<|>|=)", input_string)
    if match:
        return match.group(0)  # type: ignore
    return ""
