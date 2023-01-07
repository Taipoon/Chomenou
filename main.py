import os.path
import sys

from PyQt6.QtWidgets import QApplication
from dotenv import load_dotenv

from pyqt6.main_window import MainWindow


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
