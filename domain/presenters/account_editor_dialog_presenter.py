from domain.repositories import AccountAbstractModel
from domain.views import AccountsEditorView


class AccountsEditorDialogPresenter(object):
    def __init__(self, view: AccountsEditorView, model: AccountAbstractModel):
        self._view = view
        self._model = model
        self._view.initialize_ui()
