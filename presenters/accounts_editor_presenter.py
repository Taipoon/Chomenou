from domain.criterias import UpsertAccountCriteria
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
                criteria = UpsertAccountCriteria(
                    account_name=account.name,
                    account_name_hepburn=account.name_hepburn,
                    account_type_id=account.type_id,
                    default_amount=account.default_amount,
                )
                self._account_repository.update(account_id=account.id,
                                                update_account_criteria=criteria)
        except Exception:
            pass

    def cancel(self):
        pass
