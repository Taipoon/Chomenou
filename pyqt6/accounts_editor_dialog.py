from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLineEdit

from domain.entities import Account
from domain.exceptions import AccountNotFoundException
from domain.presenters.account_editor_dialog_presenter import AccountsEditorDialogPresenter

from domain.staticvalues import AccountTypes, Accounts
from domain.valueobjects import Amount
from infrastructure.factories import AccountFactory
from pyqt6.ui_files.ui_accounts_editor_dialog import Ui_AccountsEditorDialog


class AccountsEditorDialog(Ui_AccountsEditorDialog):
    def __init__(self):
        super().__init__()
        self._accounts = Accounts()
        self._account_types = AccountTypes()

        self._account_repository = AccountFactory()
        self._presenter = AccountsEditorDialogPresenter(view=self)

    def initialize_ui(self):
        # テキスト入力欄を整数のみ入力可能にする
        self.lineEdit_oshibori.setValidator(QIntValidator())
        self.lineEdit_kujoki.setValidator(QIntValidator())
        self.lineEdit_risueki.setValidator(QIntValidator())
        self.lineEdit_karaoke.setValidator(QIntValidator())
        self.lineEdit_chosakuken.setValidator(QIntValidator())

        # 固定費の初期値を取得してテキストフィールドに設定する
        fixed_cost_id = self._account_types.get_account_type_by_name("固定費").id
        for account in self._accounts.filter(account_type_id=fixed_cost_id):
            self.update_line_edit(account=account, amount=account.default_amount)

        # 入力欄の一番上にフォーカスを設定する
        self.lineEdit_oshibori.setFocus()

        # TODO: 保存ボタンのテキストを設定する

    def update_line_edit(self, account: Account, amount: Amount):
        """引数で指定した account の 初期金額入力欄を amount で更新します"""

        h_name = account.name_hepburn
        if not hasattr(self, "lineEdit_" + h_name):
            raise AccountNotFoundException

        edit: QLineEdit = getattr(self, "lineEdit_" + h_name)
        edit.setText(str(amount.value))
