from domain.entities import Statement, Account
from domain.valueobjects import Amount
from domain.views import BulkInsertionView
from infrastructure.factories import StatementFactory


class BulkInsertionPresenter(object):
    def __init__(self, view: BulkInsertionView):
        self._view = view
        self._view.initialize_ui()
        self._statement_repository = StatementFactory.create()

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

    def execute_registration(self, year: int, account: Account, value: int):
        """記帳を実行します"""
        for month in self._months:
            s = Statement(year=year, month=month, day=self._day,
                          account_id=account.id, amount=Amount(value))
            self._statement_repository.insert(s)
