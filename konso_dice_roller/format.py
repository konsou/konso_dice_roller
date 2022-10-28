from typing import Union

from .roll import Roll, ResultModes


def roll_as_text(roll: Roll) -> str:
    bonus = getattr(roll, "bonus", 0)
    request_bonus, after_rolls_bonus = _bonus_strings_from_bonus(bonus)
    operator_and_number = _operator_and_number_as_string(roll)

    individual_results_text = " ".join((str(r) for r in roll.individual_results))

    return (
        f"{roll.number_of_dice}d{roll.dice_sides}{request_bonus}{operator_and_number}, "
        f"tulos: [{individual_results_text}]{after_rolls_bonus} "
        f"= {as_float_if_has_decimals(roll.result)}"
    )


def roll_as_markdown_text(roll: Roll) -> str:
    bonus = getattr(roll, "bonus", 0)
    request_bonus, after_rolls_bonus = _bonus_strings_from_bonus(bonus)

    individual_results_text = " ".join((str(r) for r in roll.individual_results))

    return (
        f"`{roll.number_of_dice}d{roll.dice_sides}{request_bonus}`, "
        f"tulos: `[{individual_results_text}]{after_rolls_bonus} "
        f"= {as_float_if_has_decimals(roll.result)}`"
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


def _operator_and_number_as_string(roll: Roll) -> str:
    if (
        roll.result_mode == ResultModes.COUNT_SUCCESSES
        and roll.comparison_operator
        and roll.comparison_value
    ):
        return f"{roll.comparison_operator}{roll.comparison_value}"
    else:
        return ""


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
