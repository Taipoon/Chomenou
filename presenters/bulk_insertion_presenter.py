from domain.entities import Statement, Account
from domain.valueobjects import Amount
from domain.views import BulkInsertionView
from infrastructure.factories import StatementFactory, AccountFactory


class BulkInsertionPresenter(object):
    def __init__(self, view: BulkInsertionView):
        self._view = view
        self._view.initialize_ui()

        # 帳面リポジトリ
        self._statement_repository = StatementFactory.create()

        # データがあるすべての年度を取得
        all_years = self._statement_repository.get_all_years()
        self._view.update_years_selector(all_years)

        # すべての勘定科目を取得
        self._account_repository = AccountFactory.create()
        all_accounts = self._account_repository.all()
        self._view.update_accounts_selector(all_accounts)

        # 記帳対象となる月の集合
        self._months = set()
        # 記帳する日
        self._day = 1

    def add_month(self, month_num: int):
        """引数で指定した月を、記帳対象に追加します"""
        self._months.add(month_num)

    def remove_month(self, month_num: int):
        """引数で指定した月を、記帳対象から除外します"""
        self._months.remove(month_num)

    def change_selected_day(self, day: int):
        self._day = day

    def execute_registration(self, year: int, account: Account, value: int):
        """記帳を実行します"""
        for month in self._months:
            s = Statement(year=year, month=month, day=self._day,
                          account_id=account.id, amount=Amount(value))
            self._statement_repository.upsert(s)
