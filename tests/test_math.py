from konso_dice_roller.math import (
    greater_than_or_equal,
    less_than_or_equal,
    greater_than,
    less_than,
    equal,
)


class TestComparisons:
    def test_greater_than_or_equal_1_1(self):
        assert greater_than_or_equal(1, 1) is True

    def test_greater_than_or_equal_2_1(self):
        assert greater_than_or_equal(2, 1) is True

    def test_greater_than_or_equal_1_2(self):
        assert greater_than_or_equal(1, 2) is False

    def test_less_than_or_equal_1_1(self):
        assert less_than_or_equal(1, 1) is True

    def test_less_than_or_equal_2_1(self):
        assert less_than_or_equal(2, 1) is False

    def test_less_than_or_equal_1_2(self):
        assert less_than_or_equal(1, 2) is True

    def test_greater_than_1_1(self):
        assert greater_than(1, 1) is False

    def test_greater_than_2_1(self):
        assert greater_than(2, 1) is True

    def test_greater_than_1_2(self):
        assert greater_than(1, 2) is False

    def test_less_than_1_1(self):
        assert less_than(1, 1) is False

    def test_less_than_2_1(self):
        assert less_than(2, 1) is False

    def test_less_than_1_2(self):
        assert less_than(1, 2) is True

    def test_equal_1_1(self):
        assert equal(1, 1) is True

    def test_equal_1_2(self):
        assert equal(1, 2) is False
