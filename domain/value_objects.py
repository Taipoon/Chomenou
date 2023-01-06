import datetime


class Amount(object):
    def __init__(self, amount: int):
        self._amount = amount

    @property
    def value(self) -> int:
        return self._amount

    @property
    def value_with_yen(self) -> str:
        return str(self.value) + "円"


class StatementCreatedAt(object):
    def __init__(self, created_at: str):
        self._created_at = created_at

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def created_at_datetime(self) -> datetime.datetime:
        return datetime.datetime.strptime(self._created_at, "%Y-%m-%d %H:%M:%s")


class FiscalYear(object):
    def __init__(self, year: int):
        self._year = year

    @property
    def year(self) -> int:
        return self._year
