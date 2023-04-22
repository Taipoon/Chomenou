from domain.entities import Account, Statement
from domain.valueobjects import Amount


class MonthlyStatementSummary(object):
    def __init__(self, year: int, month: int, statements: list[Statement]):
        self._year = year
        self._month = month
        self._statements = statements

    @property
    def statements(self) -> list[Statement]:
        return self._statements

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    def get_total_amount_by_account_id(self, account_id: int) -> Amount:
        total_amount = sum([s.amount.value for s in self._statements if s.account_id == account_id])
        return Amount(total_amount)

    def get_statements_by_account_id(self, account_id: int) -> list[Statement]:
        return [s for s in self._statements if s.account_id == account_id]


class YearlyStatementSummary(object):
    def __init__(self, year: int, summaries: list[MonthlyStatementSummary]):
        self._year = year
        self._summaries = summaries

    @property
    def year(self) -> int:
        return self._year

    def get_summary_by_month(self, month: int) -> MonthlyStatementSummary or None:
        for s in self._summaries:
            if s.month == month:
                return s
        return None
