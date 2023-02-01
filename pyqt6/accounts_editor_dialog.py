import os

from PyQt6 import uic
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLineEdit

from domain.entities import AccountTypes, Account, Accounts
from domain.repositories import AccountAbstractModel
from infrastructure.sqlite import AccountSQLite
from pyqt6.common.value_error_popup import ValueErrorPopup
from pyqt6.ui_files.ui_accounts_editor_dialog import Ui_AccountsEditorDialog


class AccountsEditorDialog(Ui_AccountsEditorDialog):
    def __init__(self):
        super().__init__()
        if os.environ.get("UI_DEBUG"):
            uic.loadUi(os.path.join(os.path.dirname(__file__),
                                    "ui_files",
                                    "accountsEditorDialog.ui"), self)
        self._presenter = None
        self._initialize_ui()

    def _initialize_ui(self):
        self._presenter = AccountsEditorDialogPresenter(self, AccountSQLite())

        self.lineEdit_chosakuken.setValidator(QIntValidator())
        self.lineEdit_kujoki.setValidator(QIntValidator())
        self.lineEdit_karaoke.setValidator(QIntValidator())
        self.lineEdit_oshibori.setValidator(QIntValidator())
        self.lineEdit_risueki.setValidator(QIntValidator())

        self.accepted.connect(self._accepted)

    def _accepted(self):
        objects = self.children()
        account_amount = dict()
        for obj in objects:
            if not isinstance(obj, QLineEdit):
                continue
            name = obj.objectName().split("_")[-1]
            try:
                input_amount = int(obj.text().replace(",", ""))
            except ValueError:
                ValueErrorPopup(self, content=f"{obj.text()} は入力値として正しくありません")
                continue

            account = Accounts.get_instance_by_hepburn(name.lower())
            account_amount[account] = input_amount
        self._presenter.update_default_amounts(account_amount=account_amount)


class AccountsEditorDialogPresenter(object):
    def __init__(self, view, model: AccountAbstractModel):
        self._view = view
        self._model = model

    def get_all_account(self):
        account_types = self._model.all()
        fixed_cost_accounts = [a for a in account_types if a.type == AccountTypes.FixedCost]
        print(fixed_cost_accounts)

    def update_default_amounts(self, account_amount: dict[Account: int]):
        for account, amount in account_amount.items():
            print(account, amount)
            # self._model.update_default_amount(account=account, amount=amount)
