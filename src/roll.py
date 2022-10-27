from random import randint


class Roll:
    def __init__(self, number_of_dice: int, dice_sides: int, bonus: float) -> None:
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        self._individual_results: tuple[int, ...] = ()

        self._roll()

    def _roll(self):
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )

    @property
    def result(self) -> float:
        return sum(self.individual_results) + self.bonus

    @property
    def individual_results(self) -> tuple[float, ...]:
        return self._individual_results
