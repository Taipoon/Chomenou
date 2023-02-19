from domain.entities import Account
from domain.views import AccountsEditorView
from infrastructure.factories import AccountFactory


class AccountsEditorPresenter(object):
    def __init__(self, view: AccountsEditorView):
        self._account_repository = AccountFactory.create()

        self._view = view
        self._view.initialize_ui()

    def save(self, update_accounts: list[Account]):
        try:
            for account in update_accounts:
                self._account_repository.update_account(account_id=account.id, account=account)
        except Exception:
            pass

    def cancel(self):
        pass
