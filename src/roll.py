from random import randint


class Roll:
    def __init__(self, number_of_dice: int, dice_sides: int, bonus: float) -> None:
        self.number_of_dice = number_of_dice
        self.dice_sides = dice_sides
        self.bonus = bonus
        self._individual_results: tuple[float, ...] = ()

        self.roll()

    def __str__(self) -> str:
        return self.result_as_text

    def roll(self):
        self._individual_results = tuple(
            (randint(1, self.dice_sides) for _ in range(self.number_of_dice))
        )

    @property
    def result(self) -> float:
        return sum(self.individual_results) + self.bonus

    @property
    def individual_results(self) -> tuple[float, ...]:
        return self._individual_results

    @property
    def result_as_text(self) -> str:
        individual_results_text = " ".join((str(r) for r in self.individual_results))
        return f"Rolls: [{individual_results_text}] Result: {self.result}"