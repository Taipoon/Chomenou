import unittest

from domain.entities import Statement
from domain.repositories import IStatement
from domain.staticvalues import *
from domain.value_objects import Amount, StatementCreatedAt
from pyqt6.main_window import MainWindow, MainWindowPresenter


class StatementMock(IStatement):

    def all(self) -> list[Statement]:
        statements = [
            Statement(month=1, day=1, account=Shiire, amount=Amount(1000), created_at=StatementCreatedAt("2020-10-08")),
            Statement(month=1, day=1, account=Uriage, amount=Amount(1000), created_at=StatementCreatedAt("2020-10-08")),
            Statement(month=1, day=1, account=Uriage, amount=Amount(1000), created_at=StatementCreatedAt("2020-10-08")),
        ]
        return statements

    def get(self, month: int, day: int, account: Account):
        pass

    def insert(self, statements: list[Statement]):
        pass

    def sorted_created_at_desc(self) -> list[Statement]:
        pass


class TestMainWindowPresenter(unittest.TestCase):
    def setUp(self) -> None:
        self._presenter = MainWindowPresenter(MainWindow(), StatementMock())

    def test_scenario(self):
        with self.subTest("取得ボタンを押してテーブルを更新する"):
            self._presenter.get_button_clicked()


if __name__ == '__main__':
    unittest.main()
