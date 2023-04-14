from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QWidget

from domain.entities import Account
from domain.exceptions import AccountNotFoundException
from domain.helpers.metaclass_resolver import make_cls
from domain.shared import Signal
from domain.valueobjects import Amount
from domain.views import AccountsEditorView
from presenters.accounts_editor_presenter import AccountsEditorPresenter
from pyqt6.ui_files.ui_accounts_editor_dialog import Ui_AccountsEditorDialog


class AccountsEditorDialog(Ui_AccountsEditorDialog, AccountsEditorView, metaclass=make_cls()):
    def __init__(self):
        super().__init__()
        self._accounts = Accounts()
        self._account_types = AccountTypes()
        self._presenter = AccountsEditorPresenter(view=self)

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
        self.buttonBox.accepted.connect(self._button_box_accepted)

    def _button_box_accepted(self):
        update_accounts = []
        try:
            for name, obj in self.__dict__.items():
                if not isinstance(obj, QLineEdit):
                    continue

                if name.startswith("lineEdit_"):
                    # UI 部品名から、該当する勘定科目オブジェクトを取得
                    hepburn_name = name.split("_")[1]
                    account = Accounts().get_account_by_hepburn(hepburn=hepburn_name)

                    # 入力された金額を整数に変換する
                    input_value = obj.text()

                    updated_value = 0
                    if input_value.strip() != "":
                        updated_value = int(obj.text().replace(",", ""))

                    updated_account = Account(
                        account_id=account.id,
                        account_name=account.name,
                        account_name_hepburn=account.name_hepburn,
                        account_type=account.type,
                        default_amount=Amount(updated_value),
                    )
                    update_accounts.append(updated_account)

            # 保存処理
            self._presenter.save(update_accounts=update_accounts)
            # static value にも反映させる
            self._accounts.reset()

        except ValueError as e:
            # raise InvalidAmountException
            self.show_popup(parent=self, level=Signal.WARNING, title="値エラー", e=e)

    def update_line_edit(self, account: Account, amount: Amount):
        """引数で指定した account の 初期金額入力欄を amount で更新します"""

        h_name = account.name_hepburn
        if not hasattr(self, "lineEdit_" + h_name):
            raise AccountNotFoundException

        edit: QLineEdit = getattr(self, "lineEdit_" + h_name)
        edit.setText(str(amount.value))

    @staticmethod
    def show_popup(parent: QWidget, level: Signal, title: str, e: Exception):
        text = " | ".join(e.args)

        if level == Signal.INFO:
            QMessageBox.information(parent, title, text)
        elif level == Signal.ABOUT:
            QMessageBox.about(parent, title, text)
        elif level == Signal.WARNING:
            QMessageBox.warning(parent, title, text)
        elif level == Signal.CRITICAL:
            QMessageBox.critical(parent, title, text)
