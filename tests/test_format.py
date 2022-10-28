from unittest.mock import MagicMock

from konso_dice_roller.format import (
    roll_as_text,
    roll_as_markdown_text,
    as_float_if_has_decimals,
    number_as_string_with_sign,
    number_as_string_with_spaces_around_sign,
)
from konso_dice_roller.roll import ResultModes


class MockRoll(MagicMock):
    bonus: float = 0


class TestRollAsText:
    def test_result_shown(self):
        roll = MockRoll()
        output = roll_as_text(roll)
        assert "tulos: " in output
        assert not output.endswith("tulos: ")

    def test_correct_total_result_shown_3(self):
        roll = MockRoll(result=3)
        assert roll_as_text(roll).endswith("= 3")

    def test_correct_total_result_shown_482(self):
        roll = MockRoll(result=482)
        assert roll_as_text(roll).endswith("= 482")

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
        assert roll_as_text(roll) == "10d10, tulos: [9 8 7 6 5 4 3 2 1 0] = 45"

    def test_full_text_9876543210_plus_99(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=99,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=144,
        )
        assert roll_as_text(roll) == "10d10+99, tulos: [9 8 7 6 5 4 3 2 1 0] + 99 = 144"

    def test_full_text_9876543210_minus_87(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=-87,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=-42,
        )
        assert roll_as_text(roll) == "10d10-87, tulos: [9 8 7 6 5 4 3 2 1 0] - 87 = -42"

    def test_no_unnecessary_decimals(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=1.0,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=46.0,
        )
        assert roll_as_text(roll) == "10d10+1, tulos: [9 8 7 6 5 4 3 2 1 0] + 1 = 46"

    def test_decimals_when_needed(self):
        roll = MockRoll(
            number_of_dice=10,
            dice_sides=10,
            bonus=0.5,
            individual_results=(9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
            result=45.5,
        )
        assert (
            roll_as_text(roll) == "10d10+0.5, tulos: [9 8 7 6 5 4 3 2 1 0] + 0.5 = 45.5"
        )

    def test_6d6_gte_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=2,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator=">=",
            comparison_value=5,
        )
        assert roll_as_text(roll) == "6d6>=5, tulos: [1 2 3 4 5 6] = 2"

    def test_6d6_lte_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=5,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="<=",
            comparison_value=5,
        )
        assert roll_as_text(roll) == "6d6<=5, tulos: [1 2 3 4 5 6] = 5"

    def test_6d6_gt_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator=">",
            comparison_value=5,
        )
        assert roll_as_text(roll) == "6d6>5, tulos: [1 2 3 4 5 6] = 1"

    def test_6d6_lt_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=4,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="<",
            comparison_value=5,
        )
        assert roll_as_text(roll) == "6d6<5, tulos: [1 2 3 4 5 6] = 4"

    def test_6d6_eq_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="=",
            comparison_value=5,
        )
        assert roll_as_text(roll) == "6d6=5, tulos: [1 2 3 4 5 6] = 1"


class TestRollAsMarkdownText:
    def test_result_shown(self):
        roll = MockRoll()
        output = roll_as_markdown_text(roll)
        assert "tulos: " in output
        assert not output.endswith("tulos: ")

    def test_correct_total_result_shown_3(self):
        roll = MockRoll(result=3)
        assert roll_as_markdown_text(roll).endswith("= 3`")

    def test_correct_total_result_shown_482(self):
        roll = MockRoll(result=482)
        assert roll_as_markdown_text(roll).endswith("= 482`")

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
            == "`10d10`, tulos: `[9 8 7 6 5 4 3 2 1 0] = 45`"
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
            == "`10d10+99`, tulos: `[9 8 7 6 5 4 3 2 1 0] + 99 = 144`"
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
            == "`10d10-87`, tulos: `[9 8 7 6 5 4 3 2 1 0] - 87 = -42`"
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
            == "`10d10+1`, tulos: `[9 8 7 6 5 4 3 2 1 0] + 1 = 46`"
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
            == "`10d10+0.5`, tulos: `[9 8 7 6 5 4 3 2 1 0] + 0.5 = 45.5`"
        )

    def test_6d6_gte_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=2,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator=">=",
            comparison_value=5,
        )
        assert roll_as_markdown_text(roll) == "`6d6>=5`, tulos: `[1 2 3 4 5 6] = 2`"

    def test_6d6_lte_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=5,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="<=",
            comparison_value=5,
        )
        assert roll_as_markdown_text(roll) == "`6d6<=5`, tulos: `[1 2 3 4 5 6] = 5`"

    def test_6d6_gt_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator=">",
            comparison_value=5,
        )
        assert roll_as_markdown_text(roll) == "`6d6>5`, tulos: `[1 2 3 4 5 6] = 1`"

    def test_6d6_lt_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=4,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="<",
            comparison_value=5,
        )
        assert roll_as_markdown_text(roll) == "`6d6<5`, tulos: `[1 2 3 4 5 6] = 4`"

    def test_6d6_eq_5(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="=",
            comparison_value=5,
        )
        assert roll_as_markdown_text(roll) == "`6d6=5`, tulos: `[1 2 3 4 5 6] = 1`"

    def test_comparison_value_format_as_int_5_0(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="=",
            comparison_value=5.0,
        )
        assert roll_as_markdown_text(roll) == "`6d6=5`, tulos: `[1 2 3 4 5 6] = 1`"

    def test_comparison_value_format_as_float_5_99(self):
        roll = MockRoll(
            number_of_dice=6,
            dice_sides=6,
            bonus=0,
            individual_results=(1, 2, 3, 4, 5, 6),
            result=1,
            result_mode=ResultModes.COUNT_SUCCESSES,
            comparison_operator="=",
            comparison_value=5.99,
        )
        assert roll_as_markdown_text(roll) == "`6d6=5.99`, tulos: `[1 2 3 4 5 6] = 1`"


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
