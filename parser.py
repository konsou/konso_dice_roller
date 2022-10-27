from roll import Roll


def parse_input(input_string: str) -> Roll:
    dice, constant = _parse_constant(input_string)
    number_of_dice, dice_sides = dice.split("d")
    return Roll(
        number_of_dice=int(number_of_dice),
        dice_sides=int(dice_sides),
        bonus=float(constant),
    )


def _parse_constant(input_string: str) -> tuple[str, str]:
    split = input_string.split("+")
    try:
        return split[0], split[1]
    except IndexError:
        return split[0], "0"
