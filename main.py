import os.path
import sys

import dotenv
from PyQt6.QtWidgets import QApplication

from domain.staticvalues import AccountTypes, Accounts
from infrastructure.mock import StatementMock, AccountTypeMock, AccountMock
from infrastructure.sqlite import StatementSQLite, AccountTypeSQLite, AccountSQLite
from pyqt6.main_window import MainWindow

ACCOUNT_TYPES: AccountTypes
ACCOUNTS: Accounts


def load_envs() -> dict:
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    return dotenv.dotenv_values(dotenv_path)


def main():
    # envs = load_envs()

    # Create application instance
    app = QApplication(sys.argv)

    """
    if envs.get("REPOSITORY_DEBUG"):
        statements_repository = StatementMock()
        account_types_repository = AccountTypeMock()
        accounts_repository = AccountMock()
    else:
    """
    statements_repository = StatementSQLite()
    account_types_repository = AccountTypeSQLite()
    accounts_repository = AccountSQLite()

    account_types = AccountTypes(account_types_repository)
    accounts = Accounts(accounts_repository)

    window = MainWindow(statement_model=statements_repository,
                        account_model=accounts_repository,
                        accounts=accounts,
                        account_types=account_types)
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
