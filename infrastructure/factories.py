from domain.repositories import IAccountTypeRepository, IAccountRepository, IStatementRepository
from domain.shared import Config, Singleton
from infrastructure.mock import AccountTypeMock, AccountMock, StatementMock
from infrastructure.sqlite import AccountTypeSQLite, AccountSQLite, StatementSQLite


class AccountTypeFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IAccountTypeRepository:
        if Config.repository_debug:
            return AccountTypeMock()
        return AccountTypeSQLite()


class AccountFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IAccountRepository:
        if Config.repository_debug:
            return AccountMock()
        return AccountSQLite()


class StatementFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IStatementRepository:
        if Config.repository_debug:
            return StatementMock()
        return StatementSQLite()
