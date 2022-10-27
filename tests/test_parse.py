from unittest import TestCase

import pytest

from src.parse import parse_input


class TestParseInput(TestCase):
    def test_1d6(self):
        result = parse_input("1d6")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_2d6(self):
        result = parse_input("2d6")
        assert result.number_of_dice == 2
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_0d6(self):
        result = parse_input("0d6")
        assert result.number_of_dice == 0
        assert result.dice_sides == 6
        assert result.bonus == 0

    def test_1d10(self):
        result = parse_input("1d10")
        assert result.number_of_dice == 1
        assert result.dice_sides == 10
        assert result.bonus == 0

    def test_10d10(self):
        result = parse_input("10d10")
        assert result.number_of_dice == 10
        assert result.dice_sides == 10
        assert result.bonus == 0

    def test_10D10(self):
        result = parse_input("10D10")
        assert result.number_of_dice == 10
        assert result.dice_sides == 10
        assert result.bonus == 0

    def test_1d6plus1(self):
        result = parse_input("1d6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_5d8plus7(self):
        result = parse_input("5d8+7")
        assert result.number_of_dice == 5
        assert result.dice_sides == 8
        assert result.bonus == 7

    def test_1d6minus1(self):
        result = parse_input("1d6-1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == -1

    def test_5d20minus4(self):
        result = parse_input("5d20-4")
        assert result.number_of_dice == 5
        assert result.dice_sides == 20
        assert result.bonus == -4

    def test_leading_space(self):
        result = parse_input(" 1d6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_trailing_space(self):
        result = parse_input("1d6+1 ")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_leading_and_trailing_space(self):
        result = parse_input(" 1d6+1 ")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_before_d(self):
        result = parse_input("1 d6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_after_d(self):
        result = parse_input("1d 6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_before_and_after_d(self):
        result = parse_input("1 d 6+1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_before_plus(self):
        result = parse_input("1d6 +1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_after_plus(self):
        result = parse_input("1d6+ 1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_space_before_and_after_plus(self):
        result = parse_input("1d6 + 1")
        assert result.number_of_dice == 1
        assert result.dice_sides == 6
        assert result.bonus == 1

    def test_zero_sided_dice(self):
        with pytest.raises(ValueError) as e:
            parse_input("1d0")
        assert str(e.value) == "Invalid dice sides"

    def test_negative_sided_dice(self):
        with pytest.raises(ValueError) as e:
            parse_input("1d-4")
        assert str(e.value) == "Invalid dice sides"

    def test_no_dice_sides_given(self):
        with pytest.raises(ValueError) as e:
            parse_input("1d")
        assert str(e.value) == "Invalid dice sides"

    def test_nonsense_input(self):
        with pytest.raises(ValueError) as e:
            parse_input("asdfasdf")
        assert str(e.value) == "Invalid input"

    def test_nonsense_input_without_ds(self):
        with pytest.raises(ValueError) as e:
            parse_input("oooooooooooo")
        assert str(e.value) == "Invalid input"

    def test_nonsense_input_numbers_only(self):
        with pytest.raises(ValueError) as e:
            parse_input("111111111111")
        assert str(e.value) == "Invalid input"

    def test_nonsense_input_numbers_and_letters(self):
        with pytest.raises(ValueError) as e:
            parse_input("111FD4HGFD6K")
        assert str(e.value) == "Invalid input"

    def test_bonus_only(self):
        with pytest.raises(ValueError) as e:
            parse_input("+5")
        assert str(e.value) == "Invalid input"

    def test_non_numeric_number_of_dice(self):
        with pytest.raises(ValueError) as e:
            parse_input("zd2")
        assert str(e.value) == "Invalid input"

    def test_non_numeric_bonus(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2+g")
        assert str(e.value) == "Invalid input"

    def test_non_numeric_negative_bonus(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2-g")
        assert str(e.value) == "Invalid input"

    def test_double_bonus_signs(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2++1")
        assert str(e.value) == "Invalid input"

    def test_double_bonus_signs_negative(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2--1")
        assert str(e.value) == "Invalid input"

    def test_bonus_sign_without_value(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2+")
        assert str(e.value) == "Invalid input"

    def test_negative_bonus_sign_without_value(self):
        with pytest.raises(ValueError) as e:
            parse_input("2d2-")
        assert str(e.value) == "Invalid input"
