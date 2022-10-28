from unittest.mock import patch, PropertyMock, MagicMock

from konso_dice_roller.roll import Roll, ResultModes


class TestRoll:
    def test_roll_numeric_result_exists(self):
        roll = Roll(
            number_of_dice=1,
            dice_sides=10,
            bonus=3,
        )
        assert isinstance(roll.result, float) or isinstance(roll.result, int)

    def test_roll_total_result_matches_individual_results_6(self):
        with patch(
            "konso_dice_roller.roll.Roll.individual_results", new_callable=PropertyMock
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
            "konso_dice_roller.roll.Roll.individual_results", new_callable=PropertyMock
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
            "konso_dice_roller.roll.Roll.individual_results", new_callable=PropertyMock
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
            "konso_dice_roller.roll.Roll.individual_results", new_callable=PropertyMock
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

    def test_from_roll_info(self):
        roll_info = MagicMock(
            number_of_dice=10,
            dice_sides=20,
            bonus=1,
        )
        roll = Roll.from_roll_info(roll_info)
        assert roll.number_of_dice == 10
        assert roll.dice_sides == 20
        assert roll.bonus == 1

    def test_6d6_gte5(self):
        with patch(
            "konso_dice_roller.roll.Roll.individual_results", new_callable=PropertyMock
        ) as mock_individual_results:
            mock_individual_results.return_value = (1, 2, 3, 4, 5, 6)
            roll = Roll(
                number_of_dice=6,
                dice_sides=6,
                bonus=0,
                result_mode=ResultModes.COUNT_SUCCESSES,
                comparison_operator=">=",
                comparison_value=5,
            )
            assert roll.result == 2
