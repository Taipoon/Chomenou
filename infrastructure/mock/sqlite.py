import abc
import csv
import os.path

from domain.aggregates import YearlyStatementSummary, MonthlyStatementSummary
from domain.criterias import UpsertAccountCriteria
from domain.entities import Account, Statement, AccountType
from domain.exceptions import AccountNotFoundException
from domain.helpers.metaclass_resolver import make_cls
from domain.repositories import IStatementRepository, IAccountTypeRepository, IAccountRepository
from domain.shared import Singleton
from domain.valueobjects import Amount


class AccountTypeMock(IAccountTypeRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        self._account_type: list[AccountType] = []
        self._load_dummy_data()

    def _load_dummy_data(self):
        fake_path = os.path.join(os.path.dirname(__file__), "dummy_data/account_types.csv")
        with open(fake_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                i = int(row.get("id"))
                tn = row.get("type_name")
                tnh = row.get("type_name_hepburn")

                self._account_type.append(
                    AccountType(
                        type_id=i,
                        type_name=tn,
                        type_name_hepburn=tnh,
                    )
                )

    def all(self) -> list[AccountType]:
        return self._account_type


class AccountMock(IAccountRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        super().__init__()
        self._accounts: list[Account] = []
        self._load_dummy_data()

    def _load_dummy_data(self):
        fake_path = os.path.join(os.path.dirname(__file__), "dummy_data/accounts.csv")
        with open(fake_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                i = int(row.get("id"))
                an = row.get("account_name")
                anh = row.get("account_name_hepburn")
                ati = int(row.get("account_type_id"))
                da = Amount(int(row.get("default_amount")))

                self._accounts.append(
                    Account(
                        account_id=i,
                        account_name=an,
                        account_name_hepburn=anh,
                        account_type_id=ati,
                        default_amount=da,
                    )
                )

    def all(self) -> list[Account]:
        return self._accounts

    def find_by_id(self, account_id: int) -> Account:
        for a in self._accounts:
            if a.id == account_id:
                return a
        raise AccountNotFoundException

    def find_by_account_type_id(self, account_type_id: int) -> list[Account]:
        targets = []
        for a in self._accounts:
            if a.type_id == account_type_id:
                targets.append(a)

        if len(targets) == 0:
            raise AccountNotFoundException

        return targets

    def update(self, account_id: int, update_account_criteria: UpsertAccountCriteria):
        for i, a in enumerate(self._accounts):
            if a.id == account_id:
                new_id = len(self._accounts) + 1
                n = a.name if update_account_criteria.name is None else update_account_criteria.name
                nh = a.name_hepburn if update_account_criteria.name_hepburn is None else update_account_criteria.name_hepburn
                t = a.type_id if update_account_criteria.type_id is None else update_account_criteria.type_id
                dm = a.default_amount if update_account_criteria.default_amount is None else update_account_criteria.default_amount

                self._accounts[i] = Account(account_id=new_id, account_name=n, account_name_hepburn=nh,
                                            account_type_id=t, default_amount=dm)
                break
        else:
            raise AccountNotFoundException

    def create(self, new_account_criteria: UpsertAccountCriteria):
        self._accounts.append(
            Account(
                account_id=len(self._accounts) + 1,
                account_name=new_account_criteria.name,
                account_name_hepburn=new_account_criteria.name_hepburn,
                account_type_id=new_account_criteria.type_id,
                default_amount=new_account_criteria.default_amount,
            )
        )


class StatementMock(IStatementRepository, metaclass=make_cls(abc.ABCMeta, Singleton)):
    def __init__(self):
        self._statements: list[Statement] = []
        self._load_dummy_data()

    def _load_dummy_data(self):
        fake_path = os.path.join(os.path.dirname(__file__), "dummy_data/statements.csv")
        with open(fake_path, "r", encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                y = int(row.get("year"))
                m = int(row.get("month"))
                d = int(row.get("day"))
                ai = int(row.get("account_id"))
                am = int(row.get("amount"))

                self.upsert(Statement(year=y, month=m, day=d, account_id=ai, amount=Amount(am)))

    def get_all_years(self) -> list[int]:
        return list(set([s.year for s in self._statements]))

    def get(self, year: int or None = None, month: int or None = None,
            day: int or None = None, account: Account or None = None) -> list[Statement]:

        statements = self._statements

        if year is not None:
            statements = [s for s in statements if s.year == year]

        if month is not None:
            statements = [s for s in statements if s.month == month]

        if day is not None:
            statements = [s for s in statements if s.day == day]

        if account is not None:
            statements = [s for s in statements if s.account_id == account.id]

        return statements

    def upsert(self, statement: Statement):
        for i, s in enumerate(self._statements):
            # Update
            if s == statement:
                self._statements[i] = statement
                break
        else:
            # Insert
            self._statements.append(statement)

    def get_monthly_statement_summary(self, year: int, month: int) -> MonthlyStatementSummary:
        targets = [s for s in self._statements if s.year == year and s.month == month]
        return MonthlyStatementSummary(year=year, month=month, statements=targets)

    def get_yearly_statement_summary(self, year: int) -> YearlyStatementSummary:
        summaries = []
        for month in range(1, 13):
            summary = self.get_monthly_statement_summary(year=year, month=month)
            summaries.append(summary)

        return YearlyStatementSummary(year=year, summaries=summaries)

    def get_monthly_statement_detail(self, year: int, month: int, account: Account) -> list[Statement]:
        return [s for s in self._statements if s.account_id == account.id and s.year == year and s.month == month]
