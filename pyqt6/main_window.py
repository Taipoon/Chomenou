import os.path

from PyQt6 import uic
from PyQt6.QtWidgets import QTableWidgetItem

from domain.repositories import IStatement
from infrastructure.sqlite import StatementSQLite
from pyqt6.uifile.test_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "uifile", "test_window.ui"), self)
        self._presenter = MainWindowPresenter(self, StatementSQLite())


class MainWindowPresenter(object):
    def __init__(self, view: Ui_MainWindow, model: IStatement) -> None:
        self._view = view
        self._model = model
        self._bind()

    def _bind(self):
        self._view.getButton.clicked.connect(self.get_button_clicked)

    def get_button_clicked(self):
        statements = self._model.all(2000)

        self._view.statementTable.clear()
        self._view.statementTable.setRowCount(len(statements))

        for idx, statement in enumerate(statements):
            self._view.statementTable.setItem(idx, 0, QTableWidgetItem(statement.account.name))
            self._view.statementTable.setItem(idx, 1, QTableWidgetItem(statement.amount.comma_value_with_unit))
