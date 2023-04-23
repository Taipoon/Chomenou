import datetime

from domain.entities import Statement, Account
from domain.exceptions import InvalidAmountException
from domain.staticvalues import Accounts, AccountTypes
from domain.valueobjects import Amount
from domain.views import MainView
from infrastructure.factories import StatementFactory


class MainPresenter(object):
    def __init__(self, view: MainView):
        self._accounts = Accounts()

        self._account_types = AccountTypes()

        self._statement_repository = StatementFactory.create()

        self._view = view
        self._view.initialize_ui()

        today = datetime.date.today()
        self._selected_year = today.year
        self._selected_month = today.month
        self._selected_day = today.day
        self._update_summary_viewer(self._selected_year, self._selected_month, self._selected_day)

    def update_selected_date(self, year: int, month: int, day: int):
        """アプリケーション全体の年月日を更新し、必要に応じて変更後の年月日でサマリを更新します"""
        if self._is_date_changed(year, month, day):
            return
        # 年月日を保持する
        self._selected_year, self._selected_month, self._selected_day = year, month, day

        self._view.update_date_input_viewer(year, month, day)
        self._view.update_calender_viewer(year, month, day)

        # サマリビューの更新
        self._update_summary_viewer(year, month, day)

    def change_selected_account(self, account_name: str):
        """現在選択中の勘定科目を更新します"""
        selected_account = self._accounts.get_account_by_name(account_name)
        self._view.update_selected_account(selected_account)

    def execute_registration(self, year: int, month: int, day: int, input_text: str, account: Account):
        """記帳を行います"""
        try:
            amount = Amount(int(input_text.replace(",", "")))
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            statement = Statement(year=year, month=month, day=day,
                                  account_id=account.id, amount=amount)
            # データを新規登録する
            self._statement_repository.insert(statement=statement)
            # 入力欄をクリア
            self._view.clear_amount_entry_field()
            # サマリの更新
            self._update_summary_viewer(year, month, day)

        except ValueError:
            raise InvalidAmountException

    def _update_summary_viewer(self, year: int, month: int, day: int):
        self._update_daily_summary_viewer(year, month, day)
        self._update_monthly_summary_viewer(year, month)

    def _update_daily_summary_viewer(self, year: int, month: int, day: int):
        """日別サマリの更新"""
        statements = self._statement_repository.get_daily_account_summary(year=year, month=month, day=day)
        self._view.update_daily_summary_viewer(statements)

    def _update_monthly_summary_viewer(self, year: int, month: int):
        """月別サマリの更新"""
        summary_results = []

        statements = self._statement_repository.get_monthly_account_summary(year=year, month=month)
        for statement in statements:
            account = self._accounts.get_account_by_id(statement.account_id)
            if account is None:
                continue
            details = self._statement_repository.get_daily_total_by_account_and_month_and_year(year, month, account)
        """
            summary = MonthlyAccountSummary(account=account,
                                            total_amount=statement.amount,
                                            details=details)
            summary_results.append(summary)

        self._view.update_monthly_summary_viewer(summary_results)
        """

    def _is_date_changed(self, year: int, month: int, day: int) -> bool:
        return self._selected_year == year and self._selected_month == month and self._selected_day == day
