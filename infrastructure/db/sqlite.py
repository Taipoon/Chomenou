import sqlite3

from domain.aggregates import YearlyStatementSummary, MonthlyStatementSummary
from domain.entities import AccountType, Account, Statement
from domain.exceptions import AccountNotFoundException
from domain.repositories import IStatementRepository, IAccountTypeRepository, IAccountRepository
from domain.shared import Config
from domain.valueobjects import Amount


class SQLiteBase(object):
    def __init__(self):
        self._path = Config.sqlite_filepath
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

    def find_by_id(self, account_id: int) -> Account:
        sql = f"SELECT `a`.`id`, `a`.`account_name`, `a`.`account_name_hepburn`, " \
              f"`a`.`account_type_id`, `a`.`default_amount`, " \
              f"`at`.`type_name`, `at`.`type_name_hepburn` " \
              f"FROM `accounts` AS `a` " \
              f"LEFT JOIN `account_types` AS `at` " \
              f"ON at.id = a.account_type_id " \
              f"WHERE `a`.`id` = {account_id} " \
              f"LIMIT 1"

        cursor: sqlite3.Cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchone()

            if result is None:
                raise AccountNotFoundException

            i, an, anh, ati, da, tn, tnh = result
            a = Account(account_id=i, account_name=an, account_name_hepburn=anh,
                        account_type=AccountType(type_id=ati, type_name=tn, type_name_hepburn=tnh),
                        default_amount=Amount(da))
            return a
        finally:
            cursor.close()

    def update_account(self, account_id: int, new_account: Account):
        sql = f"UPDATE `accounts` " \
              f"SET `account_name` = '{new_account.name}', " \
              f"    `account_type_id` = {new_account.type.id}, " \
              f"    `default_amount` = {new_account.default_amount.value} " \
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
            account_id: int or None = None) -> list[Statement]:

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

        if account_id is not None:
            sql += f"AND `account_id` = {account_id} "

        sql += f"ORDER BY `year`, `month`, `day`, `account_id`, `created_at`"

        statements = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, day, account_id, total, updated_at = row
                s = Statement(year=year, month=month, day=day,
                              account_id=account_id,
                              amount=Amount(amount=total))
                statements.append(s)
        finally:
            cursor.close()
            return statements

    def upsert(self, statement: Statement):
        cursor = self.conn.cursor()
        try:
            sql = f"SELECT `amount` " \
                  f"FROM `statements` " \
                  f"WHERE (`year`, `month`, `day`, `account_id`) = " \
                  f"({statement.year}, {statement.month}, {statement.day}, {statement.account_id})"

            cursor.execute(sql)

            row = cursor.fetchone()
            if row is None:
                current_amount = 0
            else:
                current_amount = int(row[0])

            sql = f"REPLACE INTO `statements` (`year`, `month`, `day`, `account_id`, `amount`) " \
                  f"VALUES ({statement.year}, {statement.month}, {statement.day}, " \
                  f"{statement.account_id}, {statement.amount.value + current_amount})"
            cursor.execute(sql)

            self.conn.commit()
        except sqlite3.Error:
            self.conn.rollback()
        finally:
            cursor.close()

    def get_monthly_statement_summary(self, year: int, month: int) -> MonthlyStatementSummary:
        sql = f"SELECT `year`, `month`, `account_id`, SUM(`amount`) AS `total` " \
              f"FROM `statements` " \
              f"WHERE `year` = {year} AND `month` = {month} " \
              f"GROUP BY `account_id` " \
              f"ORDER BY `account_id`"
        cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, account_id, total = row
                s = Statement(year=year, month=month, day=0, account_id=account_id, amount=Amount(total))
                statements.append(s)

        finally:
            cursor.close()

            return MonthlyStatementSummary(year=year, month=month, statements=statements)

    def get_yearly_statement_summary(self, year: int) -> YearlyStatementSummary:
        monthly_summaries = []
        for month in range(1, 13):
            summary = self.get_monthly_statement_summary(year=year, month=month)
            monthly_summaries.append(summary)

        return YearlyStatementSummary(year=year, summaries=monthly_summaries)

    def get_monthly_statement_detail(self, year: int, month: int, account_id: int) -> list[Statement]:
        sql = f"SELECT `year`, `month`, `day`, `account_id`, SUM(`amount`) AS `total` " \
              f"FROM `statements` " \
              f"WHERE `year` = {year} AND `month` = {month} AND `account_id` = {account_id} " \
              f"GROUP BY `day` " \
              f"ORDER BY `day`"

        cursor = self.conn.cursor()
        statements = []
        try:
            cursor.execute(sql)
            for row in cursor:
                year, month, day, account_id, total = row
                s = Statement(year=year, month=month, day=day,
                              account_id=account_id, amount=Amount(total))

                statements.append(s)
        finally:
            cursor.close()
            return statements
