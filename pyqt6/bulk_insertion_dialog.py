from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QCheckBox

from domain.entities import Account
from domain.helpers.metaclass_resolver import make_cls
from domain.views import BulkInsertionView
from presenters.bulk_insertion_presenter import BulkInsertionPresenter
from pyqt6.ui_files.ui_bulk_insertion_dialog import Ui_BulkInsertionDialog


class BulkInsertionDialog(Ui_BulkInsertionDialog, BulkInsertionView, metaclass=make_cls()):
    def __init__(self):
        super().__init__()
        self._presenter = BulkInsertionPresenter(view=self)

    def initialize_ui(self):
        # 1月〜12月のチェックボックスのアクションの設定
        self.checkBox_month1.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month2.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month3.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month4.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month5.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month6.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month7.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month8.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month9.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month10.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month11.toggled.connect(self._checkboxes_toggled)
        self.checkBox_month12.toggled.connect(self._checkboxes_toggled)

        # 日付入力欄の設定
        self.dateEdit_dayInputSelector.dateChanged.connect(self._day_input_selector_date_changed)

        # 年度の選択ボックスの変更イベントを設定
        self.cmbBx_yearSelector.currentTextChanged.connect(self._year_selector_changed)

    def _checkboxes_toggled(self, checked):
        s = self.sender()
        if not isinstance(s, QCheckBox):
            return

        month_num = int(s.text().replace("月", ""))

        if checked:
            self._presenter.add_month(month_num=month_num)
        else:
            self._presenter.remove_month(month_num=month_num)

    def _day_input_selector_date_changed(self, date: QDate):
        """
        日の変更が行われると発火し、選択されている年度・月の状態に応じて、日選択の最大数を設定します
        :param date:
        :return:
        """
        year = self.cmbBx_yearSelector.currentText()
        self._check_maximum_date(int(year))
        self._presenter.change_selected_day(date.day())

    def _year_selector_changed(self, year: str):
        """
        年度の選択が行われると発火し、年度と選択された年に応じて、日選択の最大値を決定します
        """
        self._check_maximum_date(int(year))

    def _check_maximum_date(self, year: int):
        # 選択した年がうるう年か否か
        for child in self.grpBx_monthSelector.children():
            if not isinstance(child, QCheckBox):
                continue

            if child.text() == ["2月"] and child.isChecked():
                if QDate.isLeapYear(year):
                    # 2月が選択されており、うるう年であれば、上限値を30日に設定
                    self.dateEdit_dayInputSelector.setMaximumDate(QDate(year, 1, 30))
                else:
                    # 2月が選択されており、うるう年でなければ、上限値を29日に設定
                    self.dateEdit_dayInputSelector.setMaximumDate(QDate(year, 1, 29))
                return

            elif child.text() in ["4月", "6月", "9月", "11月"] and child.isChecked():
                # 31日が存在しない「小の月」が選択されている場合は、日選択の上限値を30日に設定
                self.dateEdit_dayInputSelector.setMaximumDate(QDate(year, 1, 30))
                return

    def update_line_edit(self, value: int):
        """金額入力欄を value で更新します"""
        self.lineEdit_amountEntryField.setText(str(value))

    def update_years_selector(self, years: list[int]):
        """年度の選択ボックスを更新します"""
        self.cmbBx_yearSelector.addItems(map(str, years))

    def update_accounts_selector(self, accounts: list[Account]):
        """勘定科目の選択ボックスを更新します"""
        self.cmbBx_accountSelector.addItems(map(lambda a: a.name, accounts))

    def set_day_input_selector_max_range(self, max_range: int):
        self.dateEdit_dayInputSelector.setMaximumDate(max_range)
