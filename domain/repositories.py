import abc

from domain.entities import AccountType, Account, Statement
from domain.valueobjects import FiscalYear


class AccountTypeAbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all(self) -> list[AccountType]:
        pass


class AccountAbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all(self) -> list[Account]:
        pass

    @abc.abstractmethod
    def get(self, account_name: str = None) -> str:
        pass

    @abc.abstractmethod
    def update_default_amount(self, account_name: str, amount: int):
        pass


class StatementAbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all(self, year: int) -> list[Statement]:
        pass

    @abc.abstractmethod
    def get(self, year: int, month: int, day: int, account: Account):
        pass

    @abc.abstractmethod
    def insert(self, year: int, statements: list[Statement]):
        pass

    @abc.abstractmethod
    def sorted_created_at_desc(self) -> list[Statement]:
        pass


class FiscalYearAbstractModel(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def all(self) -> list[FiscalYear]:
        pass
