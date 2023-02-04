import os.path
import sys

from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv

from infrastructure.mock import StatementMock
from infrastructure.sqlite import StatementSQLite
from pyqt6.main_window import MainWindow


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    app = QApplication(sys.argv)

    model = StatementSQLite()
    # model = StatementMock()
    window = MainWindow(model)

    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
