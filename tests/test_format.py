from unittest.mock import MagicMock

from src.format import roll_as_text, as_float_if_has_decimals


class MockRoll(MagicMock):
    bonus: float = 0


class TestRollAsText:
    def test_result_shown(self):
        roll = MockRoll()
        output = roll_as_text(roll)
        assert "Result: " in output
        assert not output.endswith("Result: ")

    def test_correct_total_result_shown_3(self):
        roll = MockRoll(result=3)
        assert roll_as_text(roll).endswith("Result: 3")

    def test_correct_total_result_shown_482(self):
        roll = MockRoll(result=482)
        assert roll_as_text(roll).endswith("Result: 482")

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
        assert (
            roll_as_text(roll)
            == "Request: 10d10 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 45"
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
            roll_as_text(roll)
            == "Request: 10d10+99 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 144"
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
            == "Request: 10d10-87 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: -42"
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
            roll_as_text(roll)
            == "Request: 10d10+1 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 46"
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
            == "Request: 10d10+0.5 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 45.5"
        )


def test_as_float_if_has_decimals_int():
    assert as_float_if_has_decimals(5) == 5


def test_as_float_if_has_decimals_float_with_int_value():
    result = as_float_if_has_decimals(5.0)
    assert result == 5
    assert isinstance(result, int)


def test_as_float_if_has_decimals_float():
    assert as_float_if_has_decimals(5.34) == 5.34
