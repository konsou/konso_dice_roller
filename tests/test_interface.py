from unittest.mock import patch, Mock

from konso_dice_roller.interface import (
    roll_string_from_input,
    markdown_roll_string_from_input,
)


class TestMarkdown:
    def test_validation_called(self):
        with patch("konso_dice_roller.interface.validate_roll_info") as mock_validate:
            with patch("konso_dice_roller.interface.parse_input") as mock_parse_input:
                mock_parse_input.return_value = Mock(
                    number_of_dice=5,
                    dice_sides=6,
                    bonus=3,
                )
                markdown_roll_string_from_input(
                    input_string="5d6+3",
                    number_of_dice_limit=10_000,
                    dice_sides_limit=5_000_000,
                    bonus_absolute_value_limit=100_000_000,
                )
                mock_validate.assert_called()
                assert mock_validate.call_args.kwargs["roll_info"].number_of_dice == 5
                assert mock_validate.call_args.kwargs["roll_info"].dice_sides == 6
                assert mock_validate.call_args.kwargs["roll_info"].bonus == 3
                assert mock_validate.call_args.kwargs["number_of_dice_limit"] == 10_000
                assert mock_validate.call_args.kwargs["dice_sides_limit"] == 5_000_000
                assert (
                    mock_validate.call_args.kwargs["bonus_absolute_value_limit"]
                    == 100_000_000
                )


class TestPlaintext:
    def test_validation_called(self):
        with patch("konso_dice_roller.interface.validate_roll_info") as mock_validate:
            with patch("konso_dice_roller.interface.parse_input") as mock_parse_input:
                mock_parse_input.return_value = Mock(
                    number_of_dice=5,
                    dice_sides=6,
                    bonus=3,
                )
                roll_string_from_input(
                    input_string="5d6+3",
                    number_of_dice_limit=10_000,
                    dice_sides_limit=5_000_000,
                    bonus_absolute_value_limit=100_000_000,
                )
                mock_validate.assert_called()
                assert mock_validate.call_args.kwargs["roll_info"].number_of_dice == 5
                assert mock_validate.call_args.kwargs["roll_info"].dice_sides == 6
                assert mock_validate.call_args.kwargs["roll_info"].bonus == 3
                assert mock_validate.call_args.kwargs["number_of_dice_limit"] == 10_000
                assert mock_validate.call_args.kwargs["dice_sides_limit"] == 5_000_000
                assert (
                    mock_validate.call_args.kwargs["bonus_absolute_value_limit"]
                    == 100_000_000
                )
