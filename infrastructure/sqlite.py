import os.path
import sqlite3

from domain.entities import AccountType, Account, Statement
from domain.repositories import IStatementRepository, IAccountTypeRepository, IAccountRepository
from domain.valueobjects import StatementCreatedAt, Amount


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


class AccountTypeSQLite(SQLiteBase, IAccountTypeRepository):
    def __init__(self):
        super().__init__()

    def all(self) -> list[AccountType]:
        sql = "SELECT `id`, `type_name`, `type_name_hepburn` FROM `account_types` ORDER BY `id`"
        cursor: sqlite3.Cursor = self.conn.cursor()
        account_types = []
        try:
            cursor.execute(sql)
            for row in cursor:
                type_id, type_name, type_name_hepburn = row
                account_types.append(AccountType(type_id=type_id,
                                                 type_name=type_name,
                                                 type_name_hepburn=type_name_hepburn))
        finally:
            cursor.close()
            return account_types


class AccountSQLite(SQLiteBase, IAccountRepository):

    def __init__(self):
        super().__init__()

    def all(self) -> list[Account]:
        sql = "SELECT `a`.`id`, `a`.`account_name`, `a`.`account_name_hepburn`, `a`.`account_type_id`, " \
              "`a`.`default_amount`, `at`.`type_name`, `at`.`type_name_hepburn` " \
              "FROM `accounts` AS `a` LEFT JOIN `account_types` AS `at` " \
              "ON `a`.`account_type_id` = `at`.`id` " \
              "ORDER BY `a`.`id`"

        accounts = []
        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                account_id, account_name, account_name_hepburn, \
                    account_type_id, default_amount, type_name, type_name_hepburn = row
                accounts.append(Account(account_id=account_id, account_name=account_name,
                                        account_name_hepburn=account_name_hepburn,
                                        account_type=AccountType(type_id=account_type_id,
                                                                 type_name=type_name,
                                                                 type_name_hepburn=type_name_hepburn),
                                        default_amount=Amount(default_amount)))
        finally:
            cursor.close()
            return accounts

    def update_account(self, account_id: int, account: Account):
        sql = f"UPDATE `accounts` " \
              f"SET `account_name` = '{account.name}', " \
              f"    `account_type_id` = {account.type.id}, " \
              f"    `default_amount` = {account.default_amount.value} " \
              f"WHERE `id` = {account_id}"

        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
        finally:
            cursor.close()


class StatementSQLite(SQLiteBase, IStatementRepository):
    def __init__(self):
        super().__init__()

    def get_all_years(self) -> list[int]:
        sql = f"SELECT `year` FROM `statements` GROUP BY `year` ORDER BY `year`"

        years = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                year = row[0]
                years.append(year)
        finally:
            cursor.close()
            return years

    def get(self, year: int = None, month: int = None, day: int = None,
            account: Account or None = None) -> list[Statement]:

        sql = f"SELECT `year`, `month`, `day`, `account_id`, " \
              f"amount, `created_at` " \
              f"FROM `statements` " \
              f"WHERE true "

        if year is not None:
            sql += f"AND `year` = {year} "

        if month is not None:
            sql += f"AND `month` = {month} "

        if day is not None:
            sql += f"AND `day` = {day} "

        if account is not None:
            sql += f"AND `account_id` = {account.id} "

        sql += f"ORDER BY `year`, `month`, `day`, `account_id`, `created_at`"

        statements = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, day, account_id, total, updated_at = row
                s = Statement(year=year, month=month, day=day,
                              account_id=account_id,
                              amount=Amount(amount=total),
                              created_at=StatementCreatedAt(created_at=updated_at))
                statements.append(s)
        finally:
            cursor.close()
            return statements

    def insert(self, statement: Statement):
        sql = f"INSERT INTO `statements` (`year`, `month`, `day`, `account_id`, `amount`, `created_at`) " \
              f"VALUES ({statement.year}, {statement.month}, {statement.day}, " \
              f"{statement.account_id}, {statement.amount.value}, '{statement.created_at.raw_str}')"

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
        finally:
            cursor.close()

    def get_daily_account_summary(self, year: int, month: int, day: int) -> list[Statement]:
        sql = f"SELECT `year`, `month`, `day`, `account_id`, SUM(`amount`) AS `total` " \
              f"FROM `statements` WHERE `year` = {year} AND `month` = {month} AND `day` = {day} " \
              f"GROUP BY `year`, `month`, `day`, `account_id` " \
              f"ORDER BY `account_id`"
        cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, day, account_id, total = row
                s = Statement(year=year, month=month, day=day,
                              account_id=account_id,
                              amount=Amount(total))
                statements.append(s)
        finally:
            cursor.close()
            return statements

    def get_monthly_account_summary(self, year: int, month: int) -> list[Statement]:
        sql = f"SELECT `year`, `month`, `account_id`, SUM(`amount`) AS `total`, MAX(`created_at`) AS `updated_at` " \
              f"FROM `statements` " \
              f"WHERE `year` = {year} AND `month` = {month} " \
              f"GROUP BY `account_id` " \
              f"ORDER BY `account_id`"
        cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, account_id, total, updated_at = row
                s = Statement(year=year, month=month, day=0,
                              account_id=account_id,
                              amount=Amount(total),
                              created_at=StatementCreatedAt(updated_at))
                statements.append(s)
        finally:
            cursor.close()
            return statements

    def get_details_summary_by_accounts(self, year: int, month: int, account: Account) -> list[Statement]:
        sql = f"SELECT `year`, `month`, `day`, `account_id`, " \
              f"SUM(`amount`) AS `total`, MAX(`created_at`) AS `updated_at` " \
              f"FROM `statements` " \
              f"WHERE `year` = {year} AND `month` = {month} AND `account_id` = {account.id} " \
              f"GROUP BY `day`, `account_id`"
        cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, day, account_id, total, updated_at = row
                s = Statement(year=year, month=month, day=day,
                              account_id=account_id, amount=Amount(total),
                              created_at=StatementCreatedAt(updated_at))
                statements.append(s)
        finally:
            cursor.close()
            return statements
