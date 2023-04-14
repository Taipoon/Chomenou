import sys

from PyQt6.QtWidgets import QApplication

from domain.shared import Config
from pyqt6.main_window import MainWindow


def main():
    # Create application instance
    app = QApplication(sys.argv)

    Config.parse(ini_filepath="config.ini", section="DEV")
    if Config.debug:
        print("DEBUG MODE: using fake data")

    window = MainWindow()
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
