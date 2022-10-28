# Konso's Dice Roller
A simple dice roller library I made for kicks.

## Installation
`pip install  --upgrade konso-dice-roller`

## Usage
```
from konso_dice_roller import markdown_roll_string_from_input, roll_string_from_input

if __name__ == '__main__':
    print(roll_string_from_input("3d6+3"))
    print(markdown_roll_string_from_input("2d6-2"))

    result = roll_string_from_input(
        input_string="100d1",
        number_of_dice_limit=50,
        dice_sides_limit=20,
        bonus_absolute_value_limit=1_000,
    )
```
Example output:
```
3d6+3, tulos: [6 4 5] + 3 = 18
`2d6-2`, tulos: `[2 1] - 2 = 1`
ValueError: Liian monta noppaa
```
