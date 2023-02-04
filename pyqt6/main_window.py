from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QTableWidgetItem, QTreeWidgetItem, QErrorMessage

from domain.entities import Account, Statement, Accounts
from domain.exceptions import InvalidAmountException
from domain.presenters.main_window_presenter import MainWindowPresenter
from domain.views import MainView
from pyqt6.ui_files.ui_main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, model):
        super().__init__()
        self._presenter = MainWindowPresenter(self, model)

    def initialize_ui(self):
        # 現在日時に設定
        self.dateEdit_dateInputViewer.setDate(QDate.currentDate())

        # 日付表示欄の変更イベントを設定
        self.dateEdit_dateInputViewer.dateChanged.connect(self._date_input_viewer_changed)

        # 選択中の勘定科目を「仕入」に設定
        self.label_selectedAccount.setText(Accounts.Shiire.name)

        # 日付変更ボタンのイベントを設定
        self.pshBtn_goBackOneDay.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goToday.clicked.connect(self._date_change_buttons_clicked)
        self.pshBtn_goForwardOneDay.clicked.connect(self._date_change_buttons_clicked)

        # カレンダーのクリックイベントを設定
        self.calenderWidget_calenderViewer.clicked.connect(self._calender_clicked)
        self.calenderWidget_calenderViewer.currentPageChanged.connect(self._calender_page_changed)

        # 金額入力欄のバリデーションを設定
        self.lineEdit_amountEntryField.setValidator(QIntValidator())
        self.lineEdit_amountEntryField.returnPressed.connect(self._execute_registration)

        # 記帳ボタンのクリックイベントを設定
        self.pshBtn_executeRegistration.clicked.connect(self._execute_registration)

        # 勘定科目ボタンのクリックイベント設定
        self.pshBtn_aisu.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_bihin.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_chosakuken.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_hoken.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_jidoshazei.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_karaoke.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_kokokuhi.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_kujoki.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_osakagas.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_oshibori.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_risueki.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_sakadai.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_settai.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_shiire.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_shomohin.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_shuzenhi.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_tsushinhi.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_uriage.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_yachin.clicked.connect(self._account_buttons_clicked)
        self.pshBtn_zappi.clicked.connect(self._account_buttons_clicked)

        # メニューバーのアクション設定
        # ファイル
        self.menu_file.triggered.connect(self._menu_file_triggered)
        # 編集
        self.menu_edit.triggered.connect(self._menu_edit_triggered)
        # ツール
        self.menu_tools.triggered.connect(self._menu_tools_triggered)

    def _date_change_buttons_clicked(self):
        """
        「1日戻る」「今日へ移動」「1日進む」ボタンの押下を検知し、日付入力欄とカレンダーを変更します。
        :return: None
        """
        s = self.sender()
        current_date = self.dateEdit_dateInputViewer.date()

        if s is self.pshBtn_goBackOneDay:
            d = current_date.addDays(-1)
            self._presenter.update_selected_date(d.year(), d.month(), d.day())

        elif s is self.pshBtn_goToday:
            today = QDate.currentDate()
            self._presenter.update_selected_date(today.year(), today.month(), today.day())

        elif s is self.pshBtn_goForwardOneDay:
            d = current_date.addDays(1)
            self._presenter.update_selected_date(d.year(), d.month(), d.day())

    def _date_input_viewer_changed(self):
        """
        日付入力欄の変更を検知し、カレンダーの選択日付を更新します。
        :return: None
        """
        date = self.dateEdit_dateInputViewer.date()
        y, m, d = date.year(), date.month(), date.day()
        self._presenter.update_selected_date(y, m, d)

    def _calender_clicked(self):
        """
        クリックされた日付に移動し、日付表示欄を更新します。
        :return:
        """
        date = self.calenderWidget_calenderViewer.selectedDate()
        y, m, d = date.year(), date.month(), date.day()
        self._presenter.update_selected_date(y, m, d)

    def _calender_page_changed(self, y: int, m: int):
        """
        カレンダーのページを変更すると、移動する直前に選択されていた日を保持した上で、
        移動先の年・月に移動します。同時に日付表示欄を更新します。
        :param y: 年
        :param m: 月
        :return: None
        """
        d = self.calenderWidget_calenderViewer.selectedDate().day()
        self._presenter.update_selected_date(y, m, d)

    def _execute_registration(self):
        """
        記帳します
        :return: None
        """
        date = self.dateEdit_dateInputViewer.date()
        y, m, d = date.year(), date.month(), date.day()
        text = self.lineEdit_amountEntryField.text()
        selected_account_name = self.label_selectedAccount.text()
        i = Accounts.get_instance_by_name(selected_account_name)
        try:
            self._presenter.execute_registration(y, m, d, text, i)
        except InvalidAmountException:
            self.show_error_popup()

    def _account_buttons_clicked(self):
        s = self.sender()
        a = Accounts.get_instance_by_name(s.text())
        self._presenter.change_selected_account(a)

    def _menu_file_triggered(self):
        pass

    def _menu_edit_triggered(self):
        pass

    def _menu_tools_triggered(self):
        pass

    def update_selected_account(self, account: Account):
        """現在選択されている勘定科目を表示します"""
        self.label_selectedAccount.setText(account.name)

    def update_date_input_viewer(self, y: int, m: int, d: int):
        """日付表示欄を更新します"""
        self.dateEdit_dateInputViewer.setDate(QDate(y, m, d))

    def update_calender_viewer(self, y: int, m: int, d: int):
        """カレンダーで選択されている日付を更新します"""
        self.calenderWidget_calenderViewer.setSelectedDate(QDate(y, m, d))

    def clear_amount_entry_field(self):
        """金額入力欄をリセットします"""
        self.lineEdit_amountEntryField.clear()

    def update_daily_summary_viewer(self, statements: list[Statement]):
        """明細テーブルを更新します"""
        self.tableWidget_dailySummaryViewer.clear()
        self.tableWidget_dailySummaryViewer.setHorizontalHeaderLabels(["勘定科目", "合計金額"])
        self.tableWidget_dailySummaryViewer.setRowCount(len(statements))
        for row, statement in enumerate(statements):
            self.tableWidget_dailySummaryViewer.setItem(row, 0, QTableWidgetItem(statement.account.name))
            self.tableWidget_dailySummaryViewer.setItem(row, 1, QTableWidgetItem(statement.amount.comma_value_with_unit))

    def update_monthly_summary_viewer(self, summary: dict[Account: list[Statement]]):
        """毎月の勘定科目ごとの日別合計金額を表示します"""
        self.treeWidget_monthlySummaryViewer.clear()

        account = summary.account

        top_level_item = QTreeWidgetItem()
        top_level_item.setText(0, account.name)

        for statement in summary.statements:
            item = QTreeWidgetItem()
            item.setText(0, statement.display_date)
            item.setText(1, statement.amount.comma_value_with_unit)
            top_level_item.addChild(item)

            self.treeWidget_monthlySummaryViewer.addTopLevelItem(top_level_item)

    @staticmethod
    def show_error_popup():
        dialog = QErrorMessage()
        dialog.show()
