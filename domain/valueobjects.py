import datetime


class Amount(object):
    unit_name = "円"

    def __init__(self, amount: int):
        self._amount = amount

    @property
    def value(self) -> int:
        return self._amount

    @property
    def value_with_unit(self) -> str:
        return str(self.value) + self.unit_name

    @property
    def comma_value_with_unit(self) -> str:
        return f"{self.value:,} {self.unit_name}"


class StatementCreatedAt(object):
    def __init__(self, created_at: str):
        self._created_at = created_at

    @property
    def datetime(self) -> datetime.datetime:
        return datetime.datetime.strptime(self._created_at, "%Y-%m-%d %H:%M:%S")

    @property
    def raw_str(self) -> str:
        return self._created_at

    @property
    def standard_format(self) -> str:
        return self.datetime.strftime("%Y年%m月%d日 %H時%M分%S秒")


class FiscalYear(object):
    def __init__(self, year: int):
        self._year = year

    def __str__(self):
        return f"{self.year}年"

    @property
    def year(self) -> int:
        return self._year
