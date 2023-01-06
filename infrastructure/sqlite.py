import os.path
import sqlite3

from domain.entities import AccountType, Account, Statement
from domain.repositories import IAccountType, IAccount, IStatement, IFiscalYear
from domain.value_objects import FiscalYear, StatementCreatedAt


class SQLiteBase(object):
    _db_path: str = None
    _conn: sqlite3.Connection = None

    def __init__(self, path: str = os.path.join(os.path.dirname(__file__), "db", "taipoon.db")):
        if self.__class__._db_path is None:
            self.__class__._db_path = path

        if self.__class__._conn is None:
            self.__class__._conn = sqlite3.connect(self.__class__._db_path)


class AccountTypeSQLite(SQLiteBase, IAccountType):
    def __init__(self):
        super().__init__()

    def all(self) -> list[AccountType]:
        pass


class AccountSQLite(SQLiteBase, IAccount):
    def __init__(self):
        super().__init__()

    def all(self) -> list[Account]:
        pass

    def get(self, account_name: str = None) -> str:
        pass

    def update_default_amount(self, account_name: str, amount: int):
        pass


class StatementSQLite(SQLiteBase, IStatement):
    def __init__(self):
        super().__init__()

    def all(self) -> list[Statement]:
        sql = "SELECT `month`, `day`, `account_id`, `amount`, `created_at` FROM `2000`;"
        cursor = self._conn.execute(sql)

        statements = []
        for row in cursor:
            month, day, account_id, amount, created_at = row
            s = Statement(month, day, Account(account_id), amount, StatementCreatedAt(created_at))
            statements.append(s)
        return statements

    def get(self, month: int, day: int, account: Account):
        pass

    def insert(self, statements: list[Statement]):
        pass

    def sorted_created_at_desc(self) -> list[Statement]:
        pass


class FiscalYearSQLite(SQLiteBase, IFiscalYear):
    def __init__(self):
        super().__init__()

    def all(self) -> list[FiscalYear]:
        pass
