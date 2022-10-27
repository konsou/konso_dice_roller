from unittest.mock import patch, PropertyMock

from roll import Roll


class Test:
    def test_roll_result_shown(self):
        roll = Roll(
            number_of_dice=2,
            dice_sides=6,
            bonus=0,
        )
        roll.roll()
        output = roll.result_as_text
        assert "Result: " in output
        assert not output.endswith("Result: ")

    def test_roll_correct_result_shown(self):
        with patch("roll.Roll.result", new_callable=PropertyMock) as mock_result:
            mock_result.return_value = 3
            roll = Roll(
                number_of_dice=2,
                dice_sides=6,
                bonus=0,
            )
            assert roll.result_as_text.endswith("Result: 3")

    def test_roll_numeric_result_exists(self):
        roll = Roll(
            number_of_dice=1,
            dice_sides=10,
            bonus=3,
        )
        roll.roll()
        assert isinstance(roll.result, float) or isinstance(roll.result, int)

    def test_roll_total_result_matches_individual_results_6(self):
        with patch(
            "roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (1, 2, 3)
            roll = Roll(
                number_of_dice=3,
                dice_sides=3,
                bonus=0,
            )
            roll.roll()
            assert roll.result == 1 + 2 + 3

    def test_roll_total_result_matches_individual_results_26(self):
        with patch(
            "roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (5, 6, 7, 8)
            roll = Roll(
                number_of_dice=4,
                dice_sides=10,
                bonus=0,
            )
            roll.roll()
            assert roll.result == 5 + 6 + 7 + 8

    def test_roll_individual_roll_results_exist_5d6(self):
        roll = Roll(
            number_of_dice=5,
            dice_sides=6,
            bonus=0,
        )
        roll.roll()
        assert len(roll.individual_results) == 5

    def test_roll_individual_roll_results_exist_7d8(self):
        roll = Roll(
            number_of_dice=7,
            dice_sides=8,
            bonus=0,
        )
        roll.roll()
        assert len(roll.individual_results) == 7
