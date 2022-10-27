from typing import Union

from src.roll import Roll


def roll_as_text(roll: Roll) -> str:
    bonus = getattr(roll, "bonus", 0)
    request_bonus, after_rolls_bonus = _bonus_strings_from_bonus(bonus)

    individual_results_text = " ".join((str(r) for r in roll.individual_results))

    return (
        f"Request: {roll.number_of_dice}d{roll.dice_sides}{request_bonus} "
        f"Rolls: [{individual_results_text}]{after_rolls_bonus} "
        f"Result: {as_float_if_has_decimals(roll.result)}"
    )


def _bonus_strings_from_bonus(bonus: float) -> tuple[str, str]:
    """Return:
    (request bonus, after rolls bonus)
    Request bonus: number with sign
                   e.g. "+3", "-1"
                   or empty string if zero
    After rolls bonus: number with sign and spaces before and after the sign
                       e.g. " + 3", " - 1"
                       or empty string if zero
    Numbers should be formatted as integers unless they have decimals
    In that case they should be formatted as floats"""
    if bonus:
        bonus = as_float_if_has_decimals(bonus)
        request_bonus = number_as_string_with_sign(bonus)
        after_rolls_bonus = number_as_string_with_spaces_around_sign(bonus)
    else:
        request_bonus = ""
        after_rolls_bonus = ""
    return request_bonus, after_rolls_bonus


def as_float_if_has_decimals(number: Union[int, float]) -> Union[int, float]:
    return int(number) if int(number) == number else number


def number_as_string_with_spaces_around_sign(number: float) -> str:
    """Return e.g. " + 3", " - 2" """
    number_as_string = number_as_string_with_sign(number)
    for sign in ("+", "-"):
        number_as_string = number_as_string.replace(sign, f" {sign} ")
    return number_as_string


def number_as_string_with_sign(number: float) -> str:
    """Return e.g. "+3", "-2" """
    return f"{number:+}"
