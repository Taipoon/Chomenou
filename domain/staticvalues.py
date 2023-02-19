from domain.entities import AccountType, Account
from domain.exceptions import AccountTypeNotFoundException, AccountNotFoundException
from domain.repositories import IAccountTypeRepository, IAccountRepository
from domain.shared import Singleton
from infrastructure.factories import AccountTypeFactory, AccountFactory


class AccountTypes(metaclass=Singleton):
    def __init__(self, account_type_repository: IAccountTypeRepository = AccountTypeFactory.create()):
        self._account_type_repository = account_type_repository
        self._account_types: list[AccountType] = []
        self._initialize()

    def _initialize(self):
        self._account_types = self._account_type_repository.all()

    def all(self) -> list[AccountType]:
        return self._account_types

    def get_account_type_by_name(self, name: str) -> AccountType:
        for account_type in self._account_types:
            if account_type.name == name:
                return account_type
        raise AccountTypeNotFoundException


class Accounts(metaclass=Singleton):
    def __init__(self, account_repository: IAccountRepository = AccountFactory.create()):
        self._account_repository = account_repository
        self._accounts: list[Account] = []
        self._initialize()

    def _initialize(self):
        self._accounts = self._account_repository.all()

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

    def reset(self):
        self._accounts = self._account_repository.all()
