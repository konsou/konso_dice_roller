from unittest.mock import patch, PropertyMock

from src.roll import Roll, as_float_if_has_decimals


class Test:
    def test_roll_result_shown(self):
        roll = Roll(
            number_of_dice=2,
            dice_sides=6,
            bonus=0,
        )
        output = roll.result_as_text
        assert "Result: " in output
        assert not output.endswith("Result: ")

    def test_roll_correct_total_result_shown_3(self):
        with patch("src.roll.Roll.result", new_callable=PropertyMock) as mock_result:
            mock_result.return_value = 3
            roll = Roll(
                number_of_dice=2,
                dice_sides=6,
                bonus=0,
            )
            assert roll.result_as_text.endswith("Result: 3")

    def test_roll_correct_total_result_shown_482(self):
        with patch("src.roll.Roll.result", new_callable=PropertyMock) as mock_result:
            mock_result.return_value = 482
            roll = Roll(
                number_of_dice=2,
                dice_sides=6,
                bonus=432,
            )
            assert roll.result_as_text.endswith("Result: 482")

    def test_roll_correct_individual_result_shown_12345(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (1, 2, 3, 4, 5)
            roll = Roll(
                number_of_dice=5,
                dice_sides=6,
                bonus=0,
            )
            assert "[1 2 3 4 5]" in roll.result_as_text

    def test_roll_correct_individual_result_shown_23_9954_1(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (23, 9954, 1)
            roll = Roll(
                number_of_dice=3,
                dice_sides=10_000,
                bonus=0,
            )
            assert "[23 9954 1]" in roll.result_as_text

    def test_roll_result_as_text_9876543210(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
            with patch(
                "src.roll.Roll.result", new_callable=PropertyMock
            ) as mock_result:
                mock_result.return_value = 45
                roll = Roll(
                    number_of_dice=10,
                    dice_sides=10,
                    bonus=0,
                )
                assert (
                    roll.result_as_text
                    == "Request: 10d10 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 45"
                )

    def test_roll_result_as_text_9876543210_plus_99(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
            with patch(
                "src.roll.Roll.result", new_callable=PropertyMock
            ) as mock_result:
                mock_result.return_value = 144
                roll = Roll(
                    number_of_dice=10,
                    dice_sides=10,
                    bonus=99,
                )
                assert (
                    roll.result_as_text
                    == "Request: 10d10+99 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 144"
                )

    def test_roll_result_as_text_9876543210_minus_87(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
            with patch(
                "src.roll.Roll.result", new_callable=PropertyMock
            ) as mock_result:
                mock_result.return_value = -42
                roll = Roll(
                    number_of_dice=10,
                    dice_sides=10,
                    bonus=-87,
                )
                assert (
                    roll.result_as_text
                    == "Request: 10d10-87 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: -42"
                )

    def test_roll_result_as_text_no_unnecessary_decimals(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
            with patch(
                "src.roll.Roll.result", new_callable=PropertyMock
            ) as mock_result:
                mock_result.return_value = 46.0
                roll = Roll(
                    number_of_dice=10,
                    dice_sides=10,
                    bonus=1.0,
                )
                assert (
                    roll.result_as_text
                    == "Request: 10d10+1 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 46"
                )

    def test_roll_result_as_text_decimals_when_needed(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
            with patch(
                "src.roll.Roll.result", new_callable=PropertyMock
            ) as mock_result:
                mock_result.return_value = 45.5
                roll = Roll(
                    number_of_dice=10,
                    dice_sides=10,
                    bonus=0.5,
                )
                assert (
                    roll.result_as_text
                    == "Request: 10d10+0.5 Rolls: [9 8 7 6 5 4 3 2 1 0] Result: 45.5"
                )

    def test_roll_str_equals_result_as_text(self):
        roll = Roll(
            number_of_dice=2,
            dice_sides=6,
            bonus=10,
        )
        assert roll.result_as_text == str(roll)

    def test_roll_numeric_result_exists(self):
        roll = Roll(
            number_of_dice=1,
            dice_sides=10,
            bonus=3,
        )
        assert isinstance(roll.result, float) or isinstance(roll.result, int)

    def test_roll_total_result_matches_individual_results_6(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (1, 2, 3)
            roll = Roll(
                number_of_dice=3,
                dice_sides=3,
                bonus=0,
            )
            assert roll.result == 1 + 2 + 3

    def test_roll_total_result_matches_individual_results_26(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (5, 6, 7, 8)
            roll = Roll(
                number_of_dice=4,
                dice_sides=10,
                bonus=0,
            )
            assert roll.result == 5 + 6 + 7 + 8

    def test_roll_total_result_matches_individual_results_3344_and_bonus_1(self):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (3, 3, 4, 4)
            roll = Roll(
                number_of_dice=4,
                dice_sides=4,
                bonus=1,
            )
            assert roll.result == 3 + 3 + 4 + 4 + 1

    def test_roll_total_result_matches_individual_results_2954_and_bonus_negative_5(
        self,
    ):
        with patch(
            "src.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (2, 9, 5, 4)
            roll = Roll(
                number_of_dice=4,
                dice_sides=10,
                bonus=-5,
            )
            assert roll.result == 2 + 9 + 5 + 4 - 5

    def test_roll_individual_roll_results_exist_5d6(self):
        roll = Roll(
            number_of_dice=5,
            dice_sides=6,
            bonus=0,
        )
        assert len(roll.individual_results) == 5

    def test_roll_individual_roll_results_exist_7d8(self):
        roll = Roll(
            number_of_dice=7,
            dice_sides=8,
            bonus=0,
        )
        assert len(roll.individual_results) == 7


class TestIndividualFunctions:
    def test_as_float_if_has_decimals_int(self):
        assert as_float_if_has_decimals(5) == 5

    def test_as_float_if_has_decimals_float_with_int_value(self):
        result = as_float_if_has_decimals(5.0)
        assert result == 5
        assert isinstance(result, int)

    def test_as_float_if_has_decimals_float(self):
        assert as_float_if_has_decimals(5.34) == 5.34
