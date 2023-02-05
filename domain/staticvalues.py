from domain.entities import AccountType, Account
from domain.exceptions import AccountTypeNotFoundException, AccountNotFoundException
from domain.repositories import AccountAbstractModel, AccountTypeAbstractModel


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance") or cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class AccountTypes(Singleton):
    def __init__(self, model: AccountTypeAbstractModel):
        self._model = model
        self._account_types: list[AccountType] = []
        self._initialize()

    def _initialize(self):
        self._account_types = self._model.all()

    def all(self) -> list[AccountType]:
        return self._account_types

    def get_account_type_by_name(self, name: str) -> AccountType:
        for account_type in self._account_types:
            if account_type.name == name:
                return account_type
        raise AccountTypeNotFoundException


class Accounts(Singleton):
    def __init__(self, model: AccountAbstractModel):
        self._model = model
        self._accounts: list[Account] = []
        self._initialize()

    def _initialize(self):
        self._accounts = self._model.all()

    def all(self) -> list[Account]:
        return self._accounts

    def filter(self, account_type_id: int) -> list[Account]:
        return [a for a in self._accounts if a.type.id == account_type_id]

    def get_account_by_id(self, account_id: int) -> Account:
        for account in self._accounts:
            if account.id == account_id:
                return account
        raise AccountNotFoundException

    def get_account_by_name(self, name: str) -> Account:
        for account in self._accounts:
            if account.name == name:
                return account
        raise AccountNotFoundException

    def get_account_by_hepburn(self, hepburn: str) -> Account:
        for account in self._accounts:
            if account.name_hepburn == hepburn:
                return account
        raise AccountNotFoundException