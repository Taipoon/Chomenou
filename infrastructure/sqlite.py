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
    def __init__(self, path: str = os.path.join(os.path.dirname(__file__), "db", "taipoon.db")):
        self._path = path
        self.conn: sqlite3.Connection or None = None
        self._connect()

    def _connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self._path)

    def __del__(self):
        if isinstance(self.conn, sqlite3.Connection):
            self.conn.close()


class AccountTypeSQLite(SQLiteBase, AccountTypeAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[AccountType]:
        sql = "SELECT `id`, `type_name` FROM `account_types` ORDER BY `id`"
        cursor: sqlite3.Cursor = self.conn.cursor()
        account_types = []
        try:
            cursor.execute(sql)
            for row in cursor:
                type_id, type_name = row
                account_types.append(AccountType(type_id=type_id, type_name=type_name))
        finally:
            cursor.close()
            return account_types


class AccountSQLite(SQLiteBase, AccountAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[Account]:
        return self.get()

    def get(self, accounts: list[Account] = None) -> list[Account]:
        sql = ("SELECT `a`.`id`, `a`.`account_name`, `a`.`account_type_id`, `a`.`default_amount`, `at`.`type_name`" +
               "FROM `accounts` AS `a` LEFT JOIN `account_types` AS `at`")

        conditions = []
        if accounts:
            for account in accounts:
                conditions.append("id = " + str(account.id))
            sql += " WHERE " + " AND ".join(conditions)
        print(sql)
        accounts = []
        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                account_id, account_name, account_type_id, default_amount, type_name = row
                accounts.append(Account(account_id=account_id, account_name=account_name,
                                        account_type=AccountType(type_id=account_type_id, type_name=type_name),
                                        default_amount=default_amount))
        finally:
            cursor.close()
            return accounts

    def update_default_amount(self, account_name: str, amount: int) -> bool:
        sql = f"UPDATE `accounts` SET `default_amount` = {amount} WHERE `account_name` = {account_name}"
        cursor: sqlite3.Cursor = self.conn.cursor()

        result = False
        try:
            cursor.execute(sql)
            self.conn.commit()
            result = True
        except sqlite3.Error:
            self.conn.rollback()
        finally:
            cursor.close()
            return result


class StatementSQLite(SQLiteBase, StatementAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self, year: int) -> list[Statement]:
        sql = f"SELECT `month`, `day`, `account_id`, `amount`, `created_at` FROM `{year}`"
        cursor: sqlite3.Cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                month, day, account_id, amount, created_at = row
                s = Statement(month, day, account_id, Amount(amount), StatementCreatedAt(created_at))
                statements.append(s)
        finally:
            cursor.close()
            return statements

    def get(self, year: int, month: int, day: int, account: Account = None) -> list[Statement]:
        sql = f"SELECT `month`, `day`, `account_id`, `amount`, `created_at` " \
              f"FROM `{year}` " \
              f"WHERE `month` = {month} " \
              f"AND `day` = {day}"

        if account:
            sql += f" AND `account_id` = {account.id}"

        statements = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                month, day, account_id, amount, created_at = row
                statements.append(Statement(month=month, day=day,
                                            account_id=account_id,
                                            amount=Amount(amount=amount),
                                            created_at=StatementCreatedAt(created_at=created_at)))
        finally:
            cursor.close()
            return statements

    def insert(self, year: int, statements: list[Statement]):
        sql = f"INSERT INTO `{year}` (`month`, `day`, `account_id`, `amount`, `created_at`)"

        values = []
        for statement in statements:
            values.append(f"({statement.month}, {statement.day}, {statement.account.id}, " +
                          f"{statement.amount.value}, {statement.created_at.raw_str})")

        sql += ", ".join(values)
        cursor = self.conn.cursor()
        result = False
        try:
            cursor.execute(sql)
            self.conn.commit()
            result = True
        except sqlite3.Error:
            self.conn.rollback()
        finally:
            cursor.close()
            return result


class FiscalYearSQLite(SQLiteBase, FiscalYearAbstractModel):
    def __init__(self):
        super().__init__()

    def all(self) -> list[FiscalYear]:
        sql = "SELECT `year` FROM `fiscal_years`"
        cursor: sqlite3.Cursor = self.conn.cursor()
        fiscal_years = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, = row
                fiscal_years.append(FiscalYear(year=year))
        finally:
            cursor.close()
            return fiscal_years
