import os.path
import sqlite3

from domain.entities import AccountType, Account, Statement
from domain.repositories import (
    AccountTypeAbstractModel,
    AccountAbstractModel,
    StatementAbstractModel,
    FiscalYearAbstractModel
)
from domain.valueobjects import FiscalYear, StatementCreatedAt, Amount


class SQLiteBase(object):
    _db_path: str = None
    _conn: sqlite3.Connection = None

    def __init__(self, path: str = os.path.join(os.path.dirname(__file__), "db", "taipoon.db")):
        if self.__class__._db_path is None:
            self.__class__._db_path = path

        if self.__class__._conn is None:
            self.__class__._conn = sqlite3.connect(self.__class__._db_path)

    def __del__(self):
        if self.__class__._conn:
            self.__class__._conn.close()


class AccountTypeSQLite(SQLiteBase, AccountTypeAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[AccountType]:
        pass


class AccountSQLite(SQLiteBase, AccountAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[Account]:
        pass

    def get(self, account_name: str = None) -> str:
        pass

    def update_default_amount(self, account_name: str, amount: int):
        pass


class StatementSQLite(SQLiteBase, StatementAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self, year: int) -> list[Statement]:
        sql = f"SELECT `month`, `day`, `account_id`, `amount`, `created_at` FROM `{year}`"
        cursor = self._conn.execute(sql)

        statements = []
        for row in cursor:
            month, day, account_id, amount, created_at = row
            s = Statement(month, day, account_id, Amount(amount), StatementCreatedAt(created_at))
            statements.append(s)
        return statements

    def get(self, year: int, month: int, day: int, account: Account):
        pass

    def insert(self, year: int, statements: list[Statement]):
        pass

    def sorted_created_at_desc(self) -> list[Statement]:
        pass


class FiscalYearSQLite(SQLiteBase, FiscalYearAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[FiscalYear]:
        pass
