import os
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication

from domain.repositories import StatementAbstractModel
from infrastructure.sqlite import StatementSQLite
from pyqt6.bulk_insertion_dialog import BulkInsertionDialog


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "mainWindow.ui"), self)
        # self._presenter = MainWindowPresenter(self, StatementSQLite())
        self.pshBtn_goToday.clicked.connect(self.show_bulk_insert_dialog)

    def show_bulk_insert_dialog(self):
        dialog = BulkInsertionDialog()
        dialog.exec()


class MainWindowPresenter(object):
    def __init__(self, view: MainWindow, model: StatementAbstractModel) -> None:
        self._view = view
        self._model = model
        self._bind()

    def _bind(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
