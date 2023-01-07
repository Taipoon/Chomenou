import os
from datetime import datetime

from PyQt6 import uic
from PyQt6.QtCore import QDate, QDateTime
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QPushButton, QMessageBox

from domain.entities import Accounts, Account, Statement
from domain.repositories import StatementAbstractModel
from domain.valueobjects import Amount, StatementCreatedAt
from infrastructure.sqlite import StatementSQLite
from pyqt6.ui_files.ui_main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._presenter = MainWindowPresenter(self, StatementSQLite())

        if os.environ.get("UI_DEBUG"):
            uic.loadUi(os.path.join(os.path.dirname(__file__), "ui_files", "mainWindow.ui"), self)

        self._initialize_connect_signal()
        # 選択中の選択科目
        self._selected_account: Account = Accounts.get_instance_by_name("仕入")

    def _initialize_connect_signal(self):
        # 現在日時に設定
        self.dateEdit_dateInputViewer.setDate(QDate.currentDate())

        # 日付変更ボタン
        self.pshBtn_goBackOneDay.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goToday.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goForwardOneDay.clicked.connect(self._date_change_buttons_clicked)

        # 日付表示欄の変更をカレンダーに連動させる
        self.dateEdit_dateInputViewer.dateChanged.connect(self.calenderWidget_calenderViewer.setSelectedDate)

        # カレンダーの日付選択を日付表示欄に連動させる
        self.calenderWidget_calenderViewer.clicked.connect(self.dateEdit_dateInputViewer.setDate)
        self.calenderWidget_calenderViewer.currentPageChanged.connect(self._calender_widget_current_page_changed)

        # 金額入力欄のバリデーションを設定
        self.lineEdit_amountEntryField.setValidator(QIntValidator())

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

    def _date_change_buttons_clicked(self):
        s = self.sender()
        selected_date = self.dateEdit_dateInputViewer.date()
        if s is self.pshBtn_goBackOneDay:
            self.dateEdit_dateInputViewer.setDate(selected_date.addDays(-1))
        elif s is self.pshBtn_goToday:
            self.dateEdit_dateInputViewer.setDate(QDate.currentDate())
        elif s is self.pshBtn_goForwardOneDay:
            self.dateEdit_dateInputViewer.setDate(selected_date.addDays(1))

    def _calender_widget_current_page_changed(self, year, month):
        day = self.dateEdit_dateInputViewer.date().day()
        self.dateEdit_dateInputViewer.setDate(QDate(year, month, day))

    def _account_button_clicked(self):
        s = self.sender()
        instance = Accounts.get_instance_by_name(s.text())
        if instance is None:
            QMessageBox.warning(self, "勘定科目エラー", "システムで扱えない勘定科目である可能性があります")
            return
        self._selected_account = instance

    def _execute_registration_clicked(self):
        date = self.dateEdit_dateInputViewer.date()
        try:
            amount = int(self.lineEdit_amountEntryField.text().replace(",", ""))
            if amount < 1:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "金額エラー", "1以上の整数値を入力してください")
            return

        statement = Statement(month=date.month(), day=date.day(),
                              account_id=self._selected_account.id, amount=Amount(amount),
                              created_at=StatementCreatedAt(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        self._presenter.registration_action(self.dateEdit_dateInputViewer.date().year(), statement=statement)


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
        print(self._model.get(year=year, month=month, day=day, account=None))

    def update_tree_viewer_action(self):
        # ツリーサマリの更新
        pass


