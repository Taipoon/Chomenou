from domain.entities import Statement, Account
from domain.views import StatisticsView
from infrastructure.factories import AccountFactory, AccountTypeFactory, StatementFactory


class StatisticsPresenter(object):
    def __init__(self, view: StatisticsView):
        self._view = view
        self._view.initialize_ui()

        self._account_repository = AccountFactory.create()
        self._account_type_repository = AccountTypeFactory.create()
        self._statement_repository = StatementFactory.create()

    def update_accounts_summary(self, year: int) -> dict[Account: list[Statement]]:
        accounts = self._account_repository.all()

        statement_summary = {}
        for account in accounts:
            statements = self._statement_repository.get_yearly_account_summary(year=year)
            statement_summary[account] = statements

        self._view.update_accounts_summary_bar_chart(summary=statement_summary)
