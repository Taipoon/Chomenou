from domain.repositories import IAccountTypeRepository, IAccountRepository, IStatementRepository
from domain.shared import Config, Singleton
from infrastructure.db.sqlite import AccountTypeSQLite, AccountSQLite, StatementSQLite
from infrastructure.mock.mock import AccountTypeMock, AccountMock, StatementMock


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
