from unittest import TestCase
from parser import parse_input


class Test(TestCase):
    def test_parse_input_1d6(self):
        result = parse_input("1d6")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_parse_input_2d6(self):
        result = parse_input("2d6")
        assert result.number_of_dice == 2
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_parse_input_0d6(self):
        result = parse_input("0d6")
        assert result.number_of_dice == 0
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_parse_input_1d10(self):
        result = parse_input("1d10")
        assert result.number_of_dice == 1
        assert result.dice_sides == 10
        assert result.bonus == 0

    def test_parse_input_10d10(self):
        result = parse_input("10d10")
        assert result.number_of_dice == 10
        assert result.dice_sides == 10
        assert result.bonus == 0

    def test_parse_input_1d6plus1(self):
        result = parse_input("1d6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1
