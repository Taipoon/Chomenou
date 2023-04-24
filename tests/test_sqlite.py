import sqlite3
import unittest

from domain.criterias import UpsertAccountCriteria
from domain.entities import Account, AccountType, Statement
from domain.shared import Config
from domain.valueobjects import Amount
from infrastructure.db.sqlite import AccountSQLite, AccountTypeSQLite, StatementSQLite
from tests.faker import TestDB

DUMMY_CSV_FILES = [
    "account_types.csv",
    "accounts.csv",
    "statements.csv",
]

Config.parse("../config.ini", section="DEV.FAKE")
db_path = Config.sqlite_filepath
testdb = TestDB(db_path=db_path, dummy_csv_files=DUMMY_CSV_FILES)


# noinspection NonAsciiCharacters
class TestAccountSQLite(unittest.TestCase):
    def setUp(self) -> None:
        testdb.reset()
        self.account_sqlite = AccountSQLite()

        # すべての勘定科目データを準備
        ids = [i for i in range(1, 21)]
        account_names = ["仕入", "接待", "雑費",
                         "消耗品", "家賃", "アイス",
                         "大阪ガス", "保険", "通信費",
                         "修繕費", "広告費", "自動車税",
                         "酒代", "備品", "おしぼり",
                         "駆除器", "リース植木", "著作権",
                         "カラオケ", "売上"]
        account_names_hepburn = ["shiire", "settai", "zappi",
                                 "shomohin", "yachin", "aisu",
                                 "osakagas", "hoken", "tsushinhi",
                                 "shuzenhi", "kokokuhi", "jidoshazei",
                                 "sakadai", "bihin", "oshibori",
                                 "kujoki", "risueki", "chosakuken",
                                 "karaoke", "uriage"]
        account_type_ids = [1, 1, 1,
                            1, 1, 1,
                            1, 1, 1,
                            1, 1, 1,
                            1, 1, 2,
                            2, 2, 2,
                            2, 3]
        account_types = {
            1: AccountType(type_id=1, type_name="変動費", type_name_hepburn="hendohi"),
            2: AccountType(type_id=2, type_name="固定費", type_name_hepburn="koteihi"),
            3: AccountType(type_id=3, type_name="売上", type_name_hepburn="uriage"),
        }

        self.expected_all_accounts = []
        for account_id, account_name, account_name_hepburn, type_id in zip(ids, account_names,
                                                                           account_names_hepburn,
                                                                           account_type_ids):
            amount = Amount(0)
            if account_id == 15:
                amount = Amount(8000)
            elif account_id == 17:
                amount = Amount(2500)
            elif account_id == 18:
                amount = Amount(1200)

            self.expected_all_accounts.append(Account(account_id=account_id,
                                                      account_name=account_name,
                                                      account_name_hepburn=account_name_hepburn,
                                                      account_type_id=type_id,
                                                      default_amount=amount))

    def test_すべての勘定科目を正しい順序で取得できる(self):
        got_accounts = self.account_sqlite.all()
        for e, g in zip(self.expected_all_accounts, got_accounts):
            with self.subTest(f"勘定科目ID: {g.id}, 勘定科目名: {g.name}"):
                want = [e.id, e.name, e.name_hepburn, e.type_id.id,
                        e.type_id.name, e.type_id.name_hepburn, e.default_amount.value]
                got = [g.id, g.name, g.name_hepburn, g.type_id.id,
                       g.type_id.name, g.type_id.name_hepburn, g.default_amount.value]
                self.assertSequenceEqual(want, got)

    def test_勘定科目をアップデートできる(self):
        self.account_sqlite.update(1, UpsertAccountCriteria(account_name="仕入れ",
                                                            account_name_hepburn="shiire",
                                                            account_type_id=2,
                                                            default_amount=Amount(800)))

        # 更新されたかチェックする
        conn = sqlite3.connect(db_path)
        sql = """
        SELECT `id`, `account_name`, `account_name_hepburn`, `account_type_id`, `default_amount` 
        FROM `accounts` 
        WHERE `id` = 1
        LIMIT 1"""

        cursor = conn.execute(sql)
        for row in cursor:
            i, an, anh, ati, da = row
            self.assertSequenceEqual([i, an, anh, ati, da], [1, "仕入れ", "shiire", 2, Amount(800)])


# noinspection NonAsciiCharacters
class TestAccountTypeSQLite(unittest.TestCase):
    def setUp(self) -> None:
        self.account_type_sqlite = AccountTypeSQLite()
        testdb.reset()

    def test_すべての勘定科目タイプを取得できる(self):
        got = self.account_type_sqlite.all()

        # 期待値
        wants = []
        ids = [1, 2, 3]
        account_type_names = ["変動費", "固定費", "売上"]
        account_type_names_hepburn = ["hendohi", "koteihi", "uriage"]
        for i, atn, h in zip(ids, account_type_names, account_type_names_hepburn):
            wants.append(AccountType(type_id=i, type_name=atn, type_name_hepburn=h))

        for e, g in zip(wants, got):
            self.assertSequenceEqual(
                [e.id, e.name, e.name_hepburn],
                [g.id, g.name, g.name_hepburn],
            )


# noinspection NonAsciiCharacters
class TestStatementSQLite(unittest.TestCase):
    def setUp(self) -> None:
        testdb.reset()
        self.statement_sqlite = StatementSQLite()

    def test_明細があるすべての年度を昇順で取得できる(self):
        got = self.statement_sqlite.get_all_years()
        wants = [2000, 2001, 2002, 2003, 2005]

        self.assertSequenceEqual(wants, got)

    def test_明細を追加できる(self):
        new_statement = Statement(year=2010, month=9, day=3, account_id=30, amount=Amount(3399))
        self.statement_sqlite.upsert(new_statement)


if __name__ == '__main__':
    unittest.main()
