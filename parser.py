from roll import Roll


def parse_input(input_string: str) -> Roll:
    number_of_dice, dice_sides = input_string.split("d")
    return Roll(number_of_dice=int(number_of_dice),
                dice_sides=int(dice_sides),
                bonus=0)
