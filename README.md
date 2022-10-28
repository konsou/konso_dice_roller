# Konso's Dice Roller
A simple dice roller library I made for kicks.

## Installation
`pip install  --upgrade konso-dice-roller`

## Usage
```
from konso_dice_roller import markdown_roll_string_from_input, roll_string_from_input

if __name__ == '__main__':
    print(roll_string_from_input("2d20+3"))
    print(roll_string_from_input("3d6>=5"))
    print(markdown_roll_string_from_input("3d8-2"))
    print(markdown_roll_string_from_input("2d10=2"))

    result = roll_string_from_input(
        input_string="100d1",
        number_of_dice_limit=50,
        dice_sides_limit=20,
        bonus_absolute_value_limit=1_000,
    )

```
Example output:
```
2d20+3, tulos: [10 15] + 3 = 28
3d6>=5, tulos: [3 5 3] = 1
`3d8-2`, tulos: `[3 5 3] - 2 = 9`
`2d10=2`, tulos: `[4 1] = 0`
ValueError: Liian monta noppaa
```
