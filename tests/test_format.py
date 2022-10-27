from unittest.mock import MagicMock

from src.format import (
    roll_as_text,
    roll_as_markdown_text,
    as_float_if_has_decimals,
    number_as_string_with_sign,
    number_as_string_with_spaces_around_sign,
)


class MockRoll(MagicMock):
    bonus: float = 0


class TestRollAsText:
    def test_result_shown(self):
        roll = MockRoll()
        output = roll_as_text(roll)
        assert "Tulos: " in output
        assert not output.endswith("Tulos: ")

    def test_correct_total_result_shown_3(self):
        roll = MockRoll(result=3)
        assert roll_as_text(roll).endswith("Tulos: 3")

    def test_correct_total_result_shown_482(self):
        roll = MockRoll(result=482)
        assert roll_as_text(roll).endswith("Tulos: 482")

    def test_correct_individual_result_shown_12345(self):
        roll = MockRoll(individual_results=(1, 2, 3, 4, 5))
        assert "[1 2 3 4 5]" in roll_as_text(roll)

    def test_correct_individual_result_shown_23_9954_1(self):
        roll = MockRoll(individual_results=(23, 9954, 1))
        assert "[23 9954 1]" in roll_as_text(roll)

    def test_full_text_9876543210(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=0,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=45,
        )
        assert roll_as_text(roll) == "10d10 Heitot: [9 8 7 6 5 4 3 2 1 0] Tulos: 45"

    def test_full_text_9876543210_plus_99(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=99,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=144,
        )
        assert (
            roll_as_text(roll)
            == "10d10+99 Heitot: [9 8 7 6 5 4 3 2 1 0] + 99 Tulos: 144"
        )

    def test_full_text_9876543210_minus_87(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=-87,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=-42,
        )
        assert (
            roll_as_text(roll)
            == "10d10-87 Heitot: [9 8 7 6 5 4 3 2 1 0] - 87 Tulos: -42"
        )

    def test_no_unnecessary_decimals(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=1.0,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=46.0,
        )
        assert (
            roll_as_text(roll) == "10d10+1 Heitot: [9 8 7 6 5 4 3 2 1 0] + 1 Tulos: 46"
        )

    def test_decimals_when_needed(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=0.5,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=45.5,
        )
        assert (
            roll_as_text(roll)
            == "10d10+0.5 Heitot: [9 8 7 6 5 4 3 2 1 0] + 0.5 Tulos: 45.5"
        )


class TestRollAsMarkdownText:
    def test_result_shown(self):
        roll = MockRoll()
        output = roll_as_markdown_text(roll)
        assert "Tulos: " in output
        assert not output.endswith("Tulos: ")

    def test_correct_total_result_shown_3(self):
        roll = MockRoll(result=3)
        assert roll_as_markdown_text(roll).endswith("Tulos: `3`")

    def test_correct_total_result_shown_482(self):
        roll = MockRoll(result=482)
        assert roll_as_markdown_text(roll).endswith("Tulos: `482`")

    def test_correct_individual_result_shown_12345(self):
        roll = MockRoll(individual_results=(1, 2, 3, 4, 5))
        assert "[1 2 3 4 5]" in roll_as_markdown_text(roll)

    def test_correct_individual_result_shown_23_9954_1(self):
        roll = MockRoll(individual_results=(23, 9954, 1))
        assert "[23 9954 1]" in roll_as_markdown_text(roll)

    def test_full_text_9876543210(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=0,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=45,
        )
        assert (
            roll_as_markdown_text(roll)
            == "`10d10` Heitot: `[9 8 7 6 5 4 3 2 1 0]` Tulos: `45`"
        )

    def test_full_text_9876543210_plus_99(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=99,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=144,
        )
        assert (
            roll_as_markdown_text(roll)
            == "`10d10+99` Heitot: `[9 8 7 6 5 4 3 2 1 0] + 99` Tulos: `144`"
        )

    def test_full_text_9876543210_minus_87(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=-87,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=-42,
        )
        assert (
            roll_as_markdown_text(roll)
            == "`10d10-87` Heitot: `[9 8 7 6 5 4 3 2 1 0] - 87` Tulos: `-42`"
        )

    def test_no_unnecessary_decimals(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=1.0,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=46.0,
        )
        assert (
            roll_as_markdown_text(roll)
            == "`10d10+1` Heitot: `[9 8 7 6 5 4 3 2 1 0] + 1` Tulos: `46`"
        )

    def test_decimals_when_needed(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=0.5,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=45.5,
        )
        assert (
            roll_as_markdown_text(roll)
            == "`10d10+0.5` Heitot: `[9 8 7 6 5 4 3 2 1 0] + 0.5` Tulos: `45.5`"
        )


class TestAsFloatIfHasDecimals:
    def test_int(self):
        assert as_float_if_has_decimals(5) == 5

    def test_float_with_int_value(self):
        result = as_float_if_has_decimals(5.0)
        assert result == 5
        assert isinstance(result, int)

    def test_float(self):
        assert as_float_if_has_decimals(5.34) == 5.34


class TestNumberAsString:
    def test_positive_integer(self):
        assert number_as_string_with_sign(3) == "+3"

    def test_negative_integer(self):
        assert number_as_string_with_sign(-4) == "-4"

    def test_positive_float(self):
        assert number_as_string_with_sign(5.0) == "+5.0"

    def test_negative_float(self):
        assert number_as_string_with_sign(-23.0) == "-23.0"

    def test_with_spaces_positive_integer(self):
        assert number_as_string_with_spaces_around_sign(3) == " + 3"

    def test_with_spaces_negative_integer(self):
        assert number_as_string_with_spaces_around_sign(-4) == " - 4"

    def test_with_spaces_positive_float(self):
        assert number_as_string_with_spaces_around_sign(5.0) == " + 5.0"

    def test_with_spaces_negative_float(self):
        assert number_as_string_with_spaces_around_sign(-23.0) == " - 23.0"
