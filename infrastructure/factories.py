from domain.repositories import IAccountTypeRepository, IAccountRepository, IStatementRepository
from domain.shared import Config, Singleton
from infrastructure.mock import AccountTypeMock, AccountMock, StatementMock
from infrastructure.sqlite import AccountTypeSQLite, AccountSQLite, StatementSQLite


class AccountTypeFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IAccountTypeRepository:
        if Config.is_fake:
            return AccountTypeMock()
        return AccountTypeSQLite()


class AccountFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IAccountRepository:
        if Config.is_fake:
            return AccountMock()
        return AccountSQLite()


class StatementFactory(metaclass=Singleton):
    @classmethod
    def create(cls) -> IStatementRepository:
        if Config.is_fake:
            return StatementMock()
        return StatementSQLite()
