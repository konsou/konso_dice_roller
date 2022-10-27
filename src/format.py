from typing import Union

from src.roll import Roll


def roll_as_text(roll: Roll) -> str:
    bonus = getattr(roll, "bonus", 0)
    individual_results_text = " ".join((str(r) for r in roll.individual_results))
    possible_bonus_text = f"{as_float_if_has_decimals(bonus):+}" if bonus else ""
    return (
        f"Request: {roll.number_of_dice}d{roll.dice_sides}{possible_bonus_text} "
        f"Rolls: [{individual_results_text}] "
        f"Result: {as_float_if_has_decimals(roll.result)}"
    )


def as_float_if_has_decimals(number: Union[int, float]) -> Union[int, float]:
    return int(number) if int(number) == number else number
