# Konso's Dice Roller
A simple dice roller library I made for kicks.

## Installation
`pip install  --upgrade konso-dice-roller`

## Usage
```
from konso_dice_roller import roll_string_from_input, markdown_roll_string_from_input

if __name__ == '__main__':
    print(roll_string_from_input("3d6+3"))
    print(markdown_roll_string_from_input("2d6-2"))
```
Example output:
```
3d6+3, tulos: [6 4 5] + 3 = 18
`2d6-2`, tulos: `[2 1] - 2 = 1`
```
