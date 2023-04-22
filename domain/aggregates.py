from domain.entities import Account, Statement
from domain.valueobjects import Amount


class MonthlyAccountSummary(object):
    def __init__(self, account: Account, total_amount: Amount, details: list[Statement]):
        self._id = account.id
        self._account = account
        self._total_amount = total_amount
        self._details = details

    @property
    def id(self) -> int:
        return self._id

    @property
    def account(self):
        return self._account

    @property
    def details(self):
        return self._details

    @property
    def total_amount(self) -> Amount:
        return self._total_amount
