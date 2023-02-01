import os
from datetime import datetime

from PyQt6 import uic
from PyQt6.QtCore import QDate, QObject
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QPushButton, QMessageBox, QTableWidgetItem, QTreeWidgetItem

from domain.entities import Accounts, Account, Statement
from domain.repositories import StatementAbstractModel
from domain.valueobjects import Amount, StatementCreatedAt
from infrastructure.sqlite import StatementSQLite
from pyqt6.accounts_editor_dialog import AccountsEditorDialog
from pyqt6.ui_files.ui_main_window import Ui_MainWindow
from pyqt6.bulk_insertion_dialog import BulkInsertionDialog


class MainWindow(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._presenter = MainWindowPresenter(self, StatementSQLite())

        if os.environ.get("UI_DEBUG"):
            uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "mainWindow.ui"), self)

        self._initialize_connect_signal()
        # 選択中の選択科目
        self._selected_account: Account = Accounts.get_instance_by_name("仕入")
        # Window title
        self.setWindowTitle("New Taipoon")

    def _initialize_connect_signal(self):
        # 現在日時に設定
        self.dateEdit_dateInputViewer.setDate(QDate.currentDate())

        # 日付変更ボタンのイベントを設定
        self.pshBtn_goBackOneDay.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goToday.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goForwardOneDay.clicked.connect(self._date_change_buttons_clicked)

        # 日付表示欄の変更イベントを設定
        self.dateEdit_dateInputViewer.dateChanged.connect(self._date_edit_date_input_viewer_date_changed)

        # カレンダーの日付選択イベントを日付表示欄に連動させる
        self.calenderWidget_calenderViewer.clicked.connect(self.dateEdit_dateInputViewer.setDate)
        self.calenderWidget_calenderViewer.currentPageChanged.connect(self._calender_widget_current_page_changed)

        # 金額入力欄のバリデーションを設定
        self.lineEdit_amountEntryField.setValidator(QIntValidator())
        self.lineEdit_amountEntryField.returnPressed.connect(self.pshBtn_executeRegistration.click)

        # 勘定科目選択ボタンへの紐づけ
        for element in self.__dict__.values():
            if not isinstance(element, QPushButton):
                continue
            if element in [self.pshBtn_executeRegistration, self.pshBtn_goBackOneDay,
                           self.pshBtn_goToday, self.pshBtn_goForwardOneDay, self.pshBtn_showHistory]:
                continue
            element.clicked.connect(self._account_button_clicked)

        # 記帳ボタンのアクションを設定
        self.pshBtn_executeRegistration.clicked.connect(self._execute_registration_clicked)

        # メニューバーのアクション設定
        # ファイル
        self.menu_file.triggered.connect(self._menu_file_triggered)
        # 編集
        self.menu_edit.triggered.connect(self._menu_edit_triggered)
        # ツール
        self.menu_tools.triggered.connect(self._menu_tools_triggered)

    def _date_change_buttons_clicked(self):
        """
        「1日進む」、「1日戻る」、「今日へ移動」のボタンを押すと日付入力欄を更新する。
        :return: None
        """
        s = self.sender()
        selected_date = self.dateEdit_dateInputViewer.date()
        if s is self.pshBtn_goBackOneDay:
            self.dateEdit_dateInputViewer.setDate(selected_date.addDays(-1))
        elif s is self.pshBtn_goToday:
            self.dateEdit_dateInputViewer.setDate(QDate.currentDate())
        elif s is self.pshBtn_goForwardOneDay:
            self.dateEdit_dateInputViewer.setDate(selected_date.addDays(1))

    def _date_edit_date_input_viewer_date_changed(self):
        """
        日付入力欄の更新を検知すると呼び出される。
        カレンダーの選択状態を、更新後の日付と同期する。
        :return: None
        """
        # カレンダーの表示を変更
        date = self.dateEdit_dateInputViewer.date()
        self.calenderWidget_calenderViewer.setSelectedDate(date)

        # 明細テーブルの更新
        self._presenter.update_table_viewer_action(year=date.year(),
                                                   month=date.month(),
                                                   day=date.day())

    def _calender_widget_current_page_changed(self, year, month):
        """
        カレンダーの表示月を変更すると検知すると呼び出される。
        ページ遷移先の日付は、ページ遷移前に最後に選択していた日を選択する。
        :param year: int
        :param month: int
        :return: None
        """
        # 遷移前に選択していた日を取得
        day = self.dateEdit_dateInputViewer.date().day()
        # 日付入力欄の表示を変更
        self.dateEdit_dateInputViewer.setDate(QDate(year, month, day))

    def _account_button_clicked(self):
        s: QObject = self.sender()
        instance = Accounts.get_instance_by_name(s.text())
        if instance is None:
            QMessageBox.warning(self, "勘定科目エラー", "システムで扱えない勘定科目である可能性があります")
            return
        self._selected_account = instance

        # 初期値がある場合は設定
        if instance.default_amount.value != 0:
            self.lineEdit_amountEntryField.setText(str(instance.default_amount.value))

    def _execute_registration_clicked(self):
        date = self.dateEdit_dateInputViewer.date()
        try:
            amount = int(self.lineEdit_amountEntryField.text().replace(",", ""))
            if amount < 1:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "金額エラー", "1以上の整数値を入力してください")
            self.lineEdit_amountEntryField.clear()
            self.lineEdit_amountEntryField.setFocus()
            return

        statement = Statement(month=date.month(), day=date.day(),
                              account_id=self._selected_account.id, amount=Amount(amount),
                              created_at=StatementCreatedAt(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self._presenter.registration_action(self.dateEdit_dateInputViewer.date().year(), statement=statement)
        self._presenter.update_table_viewer_action(date.year(), date.month(), date.day())
        self.lineEdit_amountEntryField.clear()
        self.lineEdit_amountEntryField.setFocus()

    def _menu_file_triggered(self, action):
        pass

    def _menu_edit_triggered(self, action):
        if action is self.action_bulkInsertion:
            open_bulk_insertion_dialog()
        elif action is self.action_editAccounts:
            open_accounts_editor_dialog()

    def _menu_tools_triggered(self, action):
        pass


def open_bulk_insertion_dialog():
    d = BulkInsertionDialog()
    d.exec()


def open_accounts_editor_dialog():
    d = AccountsEditorDialog()
    d.exec()


class MainWindowPresenter(object):
    def __init__(self, view: MainWindow, model: StatementAbstractModel) -> None:
        self._view = view
        self._model = model

    def registration_action(self, year: int, statement: Statement):
        print(year, statement)
        print(self._model.insert(year=year, statements=[statement]))
        pass

    def update_table_viewer_action(self, year: int, month: int, day: int):
        # テーブル表示の更新
        rows = self._model.get(year=year, month=month, day=day, account=None)
        self._view.tableWidget_statementsViewer.clear()
        self._view.tableWidget_statementsViewer.setRowCount(len(rows))
        self._view.tableWidget_statementsViewer.setHorizontalHeaderLabels(["勘定科目", "合計金額"])

        for row_index, row in enumerate(rows):
            self._view.tableWidget_statementsViewer.setItem(row_index, 0,
                                                            QTableWidgetItem(row.account.name))
            self._view.tableWidget_statementsViewer.setItem(row_index, 1,
                                                            QTableWidgetItem(row.amount.comma_value_with_unit))
        # ツリー表示の更新
        self.update_tree_viewer_action(year=year, month=month)

    def update_tree_viewer_action(self, year: int, month: int):
        # ツリーサマリの更新
        self._view.treeWidget_monthlySummaryViewer.clear()
        # 勘定科目ごとの合計金額を取得
        summary_by_accounts = self._model.get_monthly_account_summary(year=year, month=month)

        for summary in summary_by_accounts:
            top_level_row = QTreeWidgetItem()
            top_level_row.setText(0, summary.account.name)
            top_level_row.setText(1, summary.amount.comma_value_with_unit)

            details_by_accounts = self._model.get_details_summary_by_accounts(year=year,
                                                                              month=month,
                                                                              account_id=summary.account.id)
            for detail in details_by_accounts:
                detail_row = QTreeWidgetItem(top_level_row)
                detail_row.setText(0, detail.display_date)
                detail_row.setText(1, detail.amount.comma_value_with_unit)

            self._view.treeWidget_monthlySummaryViewer.addTopLevelItem(top_level_row)
