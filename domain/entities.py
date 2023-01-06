from domain.value_objects import StatementCreatedAt, Amount
from domain.staticvalues import *


class AccountType(object):
    def __init__(self, type_id: int, type_name: str):
        self._type_id = type_id
        self._type_name = type_name

    def __eq__(self, other):
        if not isinstance(other, AccountType):
            return False
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def id(self) -> int:
        return self._type_id

    @property
    def name(self) -> str:
        return self._type_name

# TODO: DBと同期をするためのインメモリオブジェクトと、DTOを同一視して扱おうとするからおかしい
# TODO: DBのインメモリオブジェクト（定数）は、その役割を持つものとして staticvalues.Accounts.Account()に作成
# TODO: DBからの取得値を運ぶDTOは、その役割を持つものとしてentities.AccountDTOを作成し、中で上記オブジェクトを使って条件分岐
# TODO: AccountTypeも同様に2種類定義し、それらをentities.Statementに渡して集約とする．


class Account(object):
    def __init__(self, account_id: int, account_name: str, account_type: AccountType = None,
                 default_amount: Amount = None):
        self._account_id = account_id
        self._account_name = account_name or self.name
        self._account_type = account_type or self.type
        self._default_amount = default_amount or 0

    def __eq__(self, other):
        if not isinstance(other, Account):
            return False
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def id(self) -> int:
        return self._account_id

    @property
    def name(self) -> str:
        if self == Accounts.Settai:
            return Accounts.Settai.name

        if self == Accounts.Shiire:
            return Accounts.Shiire.name

        if self == Accounts.Uriage:
            return Accounts.Uriage.name

        if self == Accounts.Oshibori:
            return Accounts.Oshibori.name

    @property
    def type(self) -> AccountType:
        if self == AccountTypes.VariableCost:
            return AccountTypes.VariableCost.name

        if self == AccountTypes.FixedCost:
            return AccountTypes.FixedCost.name

        if self == AccountTypes.Sales:
            return AccountTypes.Sales.name

    @property
    def default_amount(self) -> Amount:
        return self._default_amount


class Statement(object):
    def __init__(self, month: int, day: int, account: Account, amount: Amount.value, created_at: StatementCreatedAt):
        self._month = month
        self._day = day
        self._account = account
        self._amount = amount
        self._created_at = created_at

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @property
    def account(self) -> Account:
        return self._account

    @property
    def amount(self) -> Amount.value:
        return self._amount

    @property
    def created_at(self) -> StatementCreatedAt:
        return self._created_at
