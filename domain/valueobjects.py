from domain.exceptions import InvalidAmountException


class Amount(object):
    unit_name = "円"

    def __init__(self, amount: int):
        if amount < 0:
            raise InvalidAmountException

        self._amount = amount

    def __str__(self):
        return str(self._amount)

    def __eq__(self, other) -> bool:
        if isinstance(other, Amount):
            return self.value == other.value
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @property
    def value(self) -> int:
        return self._amount

    @property
    def value_with_unit(self) -> str:
        return str(self.value) + self.unit_name

    @property
    def comma_value_with_unit(self) -> str:
        return f"{self.value:,}{self.unit_name}"
