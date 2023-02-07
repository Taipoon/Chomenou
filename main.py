import os.path
import sys

import dotenv
from PyQt6.QtWidgets import QApplication

from domain.shared import Config
from domain.staticvalues import AccountTypes, Accounts
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

    c = Config()
    if c.ui_debug and c.repository_debug:
        print("DEBUG MODE")

    window = MainWindow()
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
