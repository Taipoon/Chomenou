import abc
import csv
import os.path

from domain.entities import Account, Statement, AccountType
from domain.exceptions import AccountNotFoundException
from domain.helpers.metaclass_resolver import make_cls
from domain.repositories import IStatementRepository, IAccountTypeRepository, IAccountRepository
from domain.shared import Singleton
from domain.valueobjects import Amount


class StatementMock(IStatementRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        self._statements = []
        self.generate_fake()

    def get_all_years(self) -> list[int]:
        return [2018, 2019, 2020, 2021, 2022, 2023]

    def generate_fake(self):
        """
        予めいくつかのダミーデータを登録しておきたい場合に呼び出します。

        """
        fake_path = os.path.join(os.path.dirname(__file__), "statements_fake.csv")
        with open(fake_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                at = row.get("created_at")

                s = Statement(
                    year=int(row.get("year")),
                    month=int(row.get("month")),
                    day=int(row.get("day")),
                    account_id=int(row.get("account_id")),
                    amount=Amount(int(row.get("amount")))
                )
                self._statements.append(s)

    def get(self, year: int or None = None, month: int or None = None,
            day: int or None = None, account: Account or None = None) -> list[Statement]:
        statement = [s for s in self._statements if s.year == year]
        if month is not None:
            statement = [s for s in statement if s.month == month]

        if day is not None:
            statement = [s for s in statement if s.day == day]

        if account is not None:
            statement = [s for s in statement if s.account_id == account.id]

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

    def get_yearly_account_summary(self, year: int) -> Statement or None:
        filtered = [s.amount.value for s in self._statements if s.year == year]
        s = Statement(year=year, month=0, day=0,
                      account_id=account.id, amount=Amount(sum(filtered)))
        return s

    def get_monthly_statement_detail(self, year: int, month: int, account: Account) -> list[Statement]:
        s = [s for s in self._statements if s.account_id == account.id and s.year == year and s.month == month]
        return s


class AccountTypeMock(IAccountTypeRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        self._account_type: list[AccountType] = []
        self._setup()

    def _setup(self):
        self._account_type = [
            AccountType(type_id=1, type_name="変動費", type_name_hepburn="hendohi"),
            AccountType(type_id=2, type_name="固定費", type_name_hepburn="koteihi"),
            AccountType(type_id=3, type_name="売上", type_name_hepburn="uriage"),
        ]

    def all(self) -> list[AccountType]:
        return self._account_type


class AccountMock(IAccountRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        super().__init__()
        self._accounts: list[Account] = []
        self._setup()

    def _setup(self):
        hendohi = AccountType(1, "変動費", "hendohi")
        koteihi = AccountType(2, "固定費", "koteihi")
        uriage = AccountType(3, "売上", "uriage")
        self._accounts = [
            # 変動費
            Account(1, "仕入", "shiire", hendohi),
            Account(2, "接待", "settai", hendohi),
            Account(3, "雑費", "zappi", hendohi),
            Account(4, "消耗品", "shomohin", hendohi),
            Account(5, "家賃", "yachin", hendohi),

            Account(6, "アイス", "aisu", hendohi),
            Account(7, "大阪ガス", "osakagas", hendohi),
            Account(8, "保険", "hoken", hendohi),
            Account(9, "通信費", "tsushinhi", hendohi),
            Account(10, "修繕費", "shuzenhi", hendohi),

            Account(11, "広告費", "kokokuhi", hendohi, Amount(8800)),
            Account(12, "自動車税", "jidoshazei", hendohi, Amount(2000)),
            Account(13, "酒代", "sakadai", hendohi, Amount(14000)),
            Account(14, "備品", "bihin", hendohi, Amount(14000)),
            # 固定費
            Account(15, "おしぼり", "oshibori", koteihi, Amount(2500)),
            Account(16, "駆除機", "kujoki", koteihi, Amount(7000)),
            Account(17, "リース植木", "risueki", koteihi, Amount(6000)),
            Account(18, "著作権", "chosakuken", koteihi, Amount(5000)),
            Account(19, "カラオケ", "karaoke", koteihi, Amount(5000)),
            # 売上
            Account(20, "売上", "uriage", uriage),
        ]
        return self._accounts

    def all(self) -> list[Account]:
        return self._accounts

    def find_by_id(self, account_id: int) -> Account:
        for a in self._accounts:
            if a.id == account_id:
                return a
        raise AccountNotFoundException

    def update_account(self, account_id: int, new_account: Account):
        for i, a in enumerate(self._accounts):
            if a.id == account_id:
                self._accounts[i] = new_account
                return
