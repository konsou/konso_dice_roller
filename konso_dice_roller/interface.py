from .format import roll_as_text, roll_as_markdown_text
from .parse import parse_input
from .roll import Roll


def roll_string_from_input(input_string: str) -> str:
    roll_info = parse_input(input_string)
    roll = Roll.from_roll_info(roll_info)
    return roll_as_text(roll)


# TODO: implement and test that the interface functions actually use validate_roll_info
# TODO: move interface functions to separate file?
def markdown_roll_string_from_input(
    input_string: str,
    number_of_dice_limit: int = 0,
    dice_sides_limit: int = 0,
    bonus_limit: int = 0,
) -> str:
    roll_info = parse_input(input_string)
    roll = Roll.from_roll_info(roll_info)
    return roll_as_markdown_text(roll)
