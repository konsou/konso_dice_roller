from .format import roll_as_text, roll_as_markdown_text
from .parse import parse_input, validate_roll_info
from .roll import Roll


def roll_string_from_input(
    input_string: str,
    number_of_dice_limit: int = 0,
    dice_sides_limit: int = 0,
    bonus_absolute_value_limit: int = 0,
) -> str:
    """Will raise a ValueError on errors"""
    roll_info = parse_input(input_string)
    validate_roll_info(
        roll_info=roll_info,
        number_of_dice_limit=number_of_dice_limit,
        dice_sides_limit=dice_sides_limit,
        bonus_absolute_value_limit=bonus_absolute_value_limit,
    )
    roll = Roll.from_roll_info(roll_info)
    return roll_as_text(roll)


def markdown_roll_string_from_input(
    input_string: str,
    number_of_dice_limit: int = 0,
    dice_sides_limit: int = 0,
    bonus_absolute_value_limit: int = 0,
) -> str:
    """Will raise a ValueError on errors"""
    roll_info = parse_input(input_string)
    validate_roll_info(
        roll_info=roll_info,
        number_of_dice_limit=number_of_dice_limit,
        dice_sides_limit=dice_sides_limit,
        bonus_absolute_value_limit=bonus_absolute_value_limit,
    )
    roll = Roll.from_roll_info(roll_info)
    return roll_as_markdown_text(roll)
