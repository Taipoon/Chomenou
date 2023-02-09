import datetime
import unittest

from domain.presenters.main_window_presenter import MainWindowPresenter
from domain.shared import Config
from domain.staticvalues import Accounts
from domain.valueobjects import Amount
from infrastructure.mock import StatementMock
from pyqt6.mock import MainViewMock


class TestMainWindowPresenter(unittest.TestCase):
    def setUp(self) -> None:
        Config.parse(force_debug=True)
        self.view = MainViewMock()
        self.presenter = MainWindowPresenter(self.view)
        self.repository = StatementMock()

    def test_update_selected_date(self):
        with self.subTest("日付を変更できる"):
            # 初期値は今日の日付
            today = datetime.datetime.today()
            self.assertEqual(self.view.calender_year, today.year)
            self.assertEqual(self.view.calender_month, today.month)
            self.assertEqual(self.view.calender_day, today.day)

            # 2000/09/03 に変更
            self.presenter.update_selected_date(2000, 9, 3)

            # 日付表示欄が正しく変更されているか
            self.assertEqual(2000, self.view.date_input_year)
            self.assertEqual(9, self.view.date_input_month)
            self.assertEqual(3, self.view.date_input_day)
            # カレンダーが正しく変更されているか
            self.assertEqual(2000, self.view.calender_year)
            self.assertEqual(9, self.view.calender_month)
            self.assertEqual(3, self.view.calender_day)

    def test_change_selected_account(self):
        with self.subTest("選択中の勘定科目を変更できる"):
            self.presenter.change_selected_account(account_name="接待")
            self.assertEqual("接待", self.view.selected_account_label)

    def test_execute_registration(self):
        with self.subTest("記帳アクションを実行できる"):

            shiire = Accounts().get_account_by_name("仕入")
            self.presenter.execute_registration(2000, 9, 3, "3000", shiire)

            # 挿入されたデータを確認
            statements = self.repository.get(year=2000)
            for s in statements:
                print(s)

            # データは1件登録されているはず
            self.assertEqual(1, len(statements))

            # 挿入した1件を取得して値をチェック
            got = statements[0]
            self.assertEqual(2000, got.year)
            self.assertEqual(9, got.month)
            self.assertEqual(3, got.day)
            self.assertEqual(Amount(3000), got.amount)


if __name__ == '__main__':
    unittest.main()
