import datetime

from domain.entities import Statement, Account
from domain.exceptions import InvalidAmountException
from domain.repositories import StatementAbstractModel
from domain.valueobjects import Amount, StatementCreatedAt
from domain.views import MainView


class MainWindowPresenter(object):
    def __init__(self, view: MainView, model: StatementAbstractModel):
        self._view = view
        self._model = model
        self._view.initialize_ui()

        self._selected_year = None
        self._selected_month = None
        self._selected_day = None

    def update_selected_date(self, year: int, month: int, day: int):
        """アプリケーション全体の年月日を更新し、必要に応じて変更後の年月日でサマリを更新します"""
        if self._is_current_date(year, month, day):
            return
        # 年月日を保持する
        self._selected_year, self._selected_month, self._selected_day = year, month, day

        self._view.update_date_input_viewer(year, month, day)
        self._view.update_calender_viewer(year, month, day)

        # サマリビューの更新
        self._update_summary_viewer(year, month, day)

    def change_selected_account(self, account: Account):
        """現在選択中の勘定科目を更新します"""
        self._view.update_selected_account(account)

    def execute_registration(self, year: int, month: int, day: int, input_text: str, account: Account):
        """記帳を行います"""
        try:
            amount = Amount(int(input_text.replace(",", "")))
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            statement = Statement(year=year, month=month, day=day,
                                  account_id=account.id, amount=amount,
                                  created_at=StatementCreatedAt(now))
            # データを新規登録する
            self._model.insert(statement=statement)
            # 入力欄をクリア
            self._view.clear_amount_entry_field()
            # サマリの更新
            self._update_summary_viewer(year, month, day)

        except ValueError:
            raise InvalidAmountException

    def _update_summary_viewer(self, year: int, month: int, day: int):
        self._update_daily_summary_viewer(year, month, day)
        self._update_monthly_summary_viewer(year, month, day)

    def _update_daily_summary_viewer(self, year: int, month: int, day: int):
        """日別サマリの更新"""
        statements = self._model.get_daily_account_summary(year=year, month=month, day=day)
        self._view.update_daily_summary_viewer(statements)

    def _update_monthly_summary_viewer(self, year: int, month: int, day: int):
        """月別サマリの更新"""
        if self._is_current_month(year, month):
            return
        # TODO: 実装
        pass

    def _is_current_date(self, year: int, month: int, day: int) -> bool:
        return self._selected_year == year and self._selected_month == month and self._selected_day == day

    def _is_current_month(self, year: int, month: int) -> bool:
        return self._selected_year == year and self._selected_month == month
