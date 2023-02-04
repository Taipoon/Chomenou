import datetime
import random

from domain.entities import Account, Statement
from domain.repositories import StatementAbstractModel
from domain.valueobjects import Amount, StatementCreatedAt


class StatementMock(StatementAbstractModel):
    def __init__(self):
        self._statements = []
        today = datetime.date.today()
        y = today.year
        m = today.month
        d = today.day
        created_at = "2000-09-03 12:13:14"
        for _ in range(30):
            ai = random.randint(1, 20)
            am = random.randint(1, 25000)

            s = Statement(year=y, month=m, day=d, account_id=ai,
                          amount=Amount(am), created_at=StatementCreatedAt(created_at))
            self._statements.append(s)

    def get(self, year: int, month: int, day: int, account: Account or None) -> list[Statement]:
        statement = [s for s in self._statements if s.year == year]
        if month is not None:
            statement = [s for s in statement if s.month == month]
        if day is not None:
            statement = [s for s in statement if s.day == day]
        if account is not None:
            statement = [s for s in statement if s.account.id == account.id]
        return statement

    def insert(self, statement: Statement):
        self._statements.append(statement)

    def get_daily_account_summary(self, year: int, month: int, day: int) -> list[Statement]:
        account_ids = set([s.account_id for s in self._statements])
        daily_summary = []

        statements = [s for s in self._statements if s.year == year and s.month == month and s.day == day]
        for account_id in account_ids:
            total = sum([s.amount.value for s in statements if s.account_id == account_id])
            daily_summary.append(Statement(year=year, month=month, day=day,
                                           account_id=account_id, amount=Amount(total)))
        return daily_summary

    def get_monthly_account_summary(self, year: int, month: int) -> list[Statement]:
        account_ids = set([s.account_id for s in self._statements])
        monthly_summary = []
        for account_id in account_ids:
            total = sum([s.amount.value for s in self._statements if s.account_id == account_id])
            monthly_summary.append(Statement(year=year, month=month, day=0,
                                             account_id=account_id, amount=Amount(total)))
        return sorted(monthly_summary, key=lambda s: s.account_id)

    def get_details_summary_by_accounts(self, year: int, month: int, account: Account) -> list[Statement]:
        s = [s for s in self._statements if s.account_id == account.id and s.year == year and s.month == month]
        return s
