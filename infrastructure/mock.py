import datetime
import random

from domain.entities import Account, Statement, AccountType
from domain.repositories import IStatementRepository, IAccountTypeRepository, IAccountRepository
from domain.valueobjects import Amount, StatementCreatedAt


class StatementMock(IStatementRepository):
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

    def get_details_summary_by_accounts(self, year: int, month: int, account: Account) -> list[Statement]:
        s = [s for s in self._statements if s.account_id == account.id and s.year == year and s.month == month]
        return s


class AccountTypeMock(IAccountTypeRepository):
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


class AccountMock(IAccountRepository):
    def __init__(self):
        self._accounts: list[Account] = []
        self._setup()

    def _setup(self):
        hendohi = AccountType(1, "変動費", "hendohi")
        koteihi = AccountType(2, "固定費", "koteihi")
        uriage = AccountType(3, "売上", "uriage")
        self._accounts = [
            # 変動費
            Account(1, "仕入", "shiire", hendohi, 0),
            Account(2, "接待", "settai", hendohi, 0),
            Account(3, "雑費", "zappi", hendohi, 0),
            Account(4, "消耗品", "shomohin", hendohi, 0),
            Account(5, "家賃", "yachin", hendohi, 0),

            Account(6, "アイス", "aisu", hendohi, 0),
            Account(7, "大阪ガス", "osakagas", hendohi, 0),
            Account(8, "保険", "hoken", hendohi, 0),
            Account(9, "通信費", "tsushinhi", hendohi, 0),
            Account(10, "修繕費", "shuzenhi", hendohi, 0),

            Account(11, "広告費", "kokokuhi", hendohi, 8800),
            Account(12, "自動車税", "jidoshazei", hendohi, 2000),
            Account(13, "酒代", "sakadai", hendohi, 14000),
            Account(14, "備品", "bihin", hendohi, 14000),

            # 固定費
            Account(15, "おしぼり", "oshibori", koteihi, 8000),
            Account(16, "駆除機", "kujoki", koteihi, 7000),
            Account(17, "リース植木", "risueki", koteihi, 6000),
            Account(18, "著作権", "chosakuken", koteihi, 5000),
            Account(19, "カラオケ", "karaoke", koteihi, 5000),

            Account(20, "売上", "uriage", uriage, 0)
        ]
        return self._accounts

    def all(self) -> list[Account]:
        return self._accounts

    def update_account(self, account_id: int, account: Account):
        for i, a in enumerate(self._accounts):
            if a.id == account_id:
                self._accounts[i] = account
                return
