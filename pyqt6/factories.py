from domain.shared import Singleton, Config
from pyqt6.accounts_editor_dialog import AccountsEditorDialog
from pyqt6.mock import AccountsEditorMock


class AccountsEditorFactory(metaclass=Singleton):
    @classmethod
    def create(cls):
        if Config.is_fake:
            return AccountsEditorMock()
        return AccountsEditorDialog()
