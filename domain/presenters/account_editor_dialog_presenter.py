from domain.views import AccountsEditorView
from infrastructure.factories import AccountTypeFactory


class AccountsEditorDialogPresenter(object):
    def __init__(self, view: AccountsEditorView):
        self._account_type_repository = AccountTypeFactory()

        self._view = view
        self._view.initialize_ui()
