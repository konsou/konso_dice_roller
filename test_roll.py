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

    def test_roll_numeric_result_exists(self):
        roll = Roll(
            number_of_dice=1,
            dice_sides=10,
            bonus=3,
        )
        roll.roll()
        assert isinstance(roll.result, float) or isinstance(roll.result, int)
