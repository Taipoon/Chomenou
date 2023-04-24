import datetime

from domain.aggregates import MonthlyStatementSummary
from domain.entities import Statement, Account
from domain.valueobjects import Amount
from domain.views import MainView, AccountsEditorView


class MainViewMock(MainView):
    def __init__(self):
        self.calender_year = 2000
        self.calender_month = 1
        self.calender_day = 1

        self.date_input_year = 2000
        self.date_input_month = 1
        self.date_input_day = 1

        self.selected_account_label = "仕入"
        self.amount_field_line_edit = ""

    def initialize_ui(self):
        today = datetime.datetime.today()
        self.calender_year = self.date_input_year = today.year
        self.calender_month = self.date_input_month = today.month
        self.calender_day = self.date_input_day = today.day

    def update_selected_account(self, account: Account):
        self.selected_account_label = account.name

    def update_date_input_viewer(self, y: int, m: int, d: int):
        self.date_input_year, self.date_input_month, self.date_input_day = y, m, d

    def update_calender_viewer(self, y: int, m: int, d: int):
        self.calender_year, self.calender_month, self.calender_day = y, m, d

    def clear_amount_entry_field(self):
        self.selected_account_label = ""

    def set_amount_entry_field(self, value: int):
        self.amount_field_line_edit = str(value)

    def update_daily_summary_viewer(self, statements: list[Statement]):
        pass

    def update_monthly_summary_viewer(self, summary: MonthlyStatementSummary):
        pass


class AccountsEditorMock(AccountsEditorView):
    def initialize_ui(self):
        pass

    def update_line_edit(self, account: Account, amount: Amount):
        pass

    def exec(self):
        pass
