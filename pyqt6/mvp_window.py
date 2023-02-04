import abc
import sys
from typing import List

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QApplication

from pyqt6.ui_files.user_manager import Ui_UserManager


class User(object):
    """
    ユーザーを表すエンティティです
    """

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def age_str(self):
        return str(self._age)


class UserManagerViewInterface(abc.ABC):
    """
    MainView はこのインターフェースを実装します
    """
    @abc.abstractmethod
    def initialize(self):
        """
        Viewの初期化を行います
        :return: None
        """
        pass

    @abc.abstractmethod
    def update_user_list(self, users: List[User]) -> List[User]:
        """
        ユーザーの表示を更新します
        :param users:
        :return: None
        """
        pass

    @abc.abstractmethod
    def user_name_line_edit_reset(self):
        """
        ユーザー名入力欄をリセットします
        :return: None
        """
        pass

    @abc.abstractmethod
    def update_calender_date(self, year: int, month: int, day: int):
        pass

    @abc.abstractmethod
    def update_date_edit_date(self, year: int, month: int, day: int):
        pass

    @abc.abstractmethod
    def new_user_name_line_edit_reset(self):
        pass


class AbstractUserModel(abc.ABC):
    """
    ユーザーを取得する抽象モデルを表します
    """
    @abc.abstractmethod
    def all(self) -> List[User]:
        pass

    @abc.abstractmethod
    def select_by_name(self, name: str) -> List[User]:
        pass

    @abc.abstractmethod
    def add_user(self, name: str, age: int) -> List[User]:
        pass


class UserManagerWindow(Ui_UserManager):
    """
    UserManagerWindow は UserManagerViewInterface を実装します。
    GUI は PyQt6 実装されています。
    """
    def __init__(self, model: AbstractUserModel):
        super().__init__()
        self._presenter = UserManagerPresenter(self, model=model)

    def initialize(self):
        """
        UIの初期化とスロットとの接続を行います
        :return: None
        """
        self.pushButton_getAllUsers.clicked.connect(lambda: self._presenter.get_all_users())
        self.pushButton_searchByUserName.clicked.connect(
            lambda: self._presenter.search_by_name(self.lineEdit_userName.text()),
        )
        self.dateEdit.dateChanged.connect(lambda: self._date_edit_changed())
        self.calendarWidget.clicked.connect(lambda: self._calender_selected_date_changed())
        self.calendarWidget.currentPageChanged.connect(lambda y, m: self._calender_current_page_changed(y, m))

        self.pushButton_addUser.clicked.connect(lambda: self._add_user())

    def _add_user(self):
        name = self.lineEdit_newUserName.text()
        age = self.spinBox_age.text()
        self._presenter.add_new_user(name, age)

    def _date_edit_changed(self):
        date = self.dateEdit.date()
        self._presenter.update_calender(date.year(), date.month(), date.day())

    def _calender_selected_date_changed(self):
        date = self.calendarWidget.selectedDate()
        self._presenter.update_date_edit(date.year(), date.month(), date.day())

    def _calender_current_page_changed(self, y, m):
        d = self.dateEdit.date().day()
        self._presenter.update_date_edit(y, m, d)

    def update_user_list(self, users: List[User]):
        """
        リストウィジェットにユーザーのリストを表示します。
        :param users:
        :return: None
        """
        self.tableWidget_userList.clear()
        self.tableWidget_userList.setHorizontalHeaderLabels(["名前", "年齢"])
        self.tableWidget_userList.setRowCount(len(users))
        for row, user in enumerate(users):
            self.tableWidget_userList.setItem(row, 0, QTableWidgetItem(user.name))
            self.tableWidget_userList.setItem(row, 1, QTableWidgetItem(user.age_str))

    def user_name_line_edit_reset(self):
        self.lineEdit_userName.clear()

    def update_calender_date(self, year: int, month: int, day: int):
        self.calendarWidget.setSelectedDate(QDate(year, month, day))

    def update_date_edit_date(self, year: int, month: int, day: int):
        self.dateEdit.setDate(QDate(year, month, day))

    def new_user_name_line_edit_reset(self):
        self.lineEdit_newUserName.clear()


class UserManagerPresenter(object):
    """
    MainView の ロジックを担います
    """
    def __init__(self, view: UserManagerViewInterface, model: AbstractUserModel):
        self._view = view
        self._model = model
        self._view.initialize()

    def get_all_users(self):
        """
        ユーザーの一覧を取得し、ユーザーリストを更新します
        :return:
        """
        users = self._model.all()
        self._view.update_user_list(users)
        self._view.user_name_line_edit_reset()

    def search_by_name(self, name: str):
        """
        ユーザーを名前で絞り込んで、リストを更新します
        :param name: ユーザー名
        :return:
        """
        users = self._model.select_by_name(name)
        self._view.update_user_list(users)

    def update_calender(self, year: int, month: int, day: int):
        """
        カレンダーの選択された日付を更新します
        :param year: 年
        :param month: 月
        :param day: 日
        :return: None
        """
        self._view.update_calender_date(year, month, day)

    def update_date_edit(self, year: int, month: int, day: int):
        """
        日付入力欄の選択された日付を更新します
        :param year: 年
        :param month: 月
        :param day: 日
        :return: None
        """
        self._view.update_date_edit_date(year, month, day)

    def add_new_user(self, name: str, age: int):
        users = self._model.add_user(name, age)
        self._view.update_user_list(users)
        self._view.new_user_name_line_edit_reset()


class UserModel(AbstractUserModel):
    def __init__(self):
        self._user = [
            User("Taiki", 23),
            User("Hoge", 18),
            User("Piyo", 42),
        ]

    def select_by_name(self, name: str) -> List[User]:
        return [u for u in self._user if u.name.find(name) != -1]

    def all(self) -> List[User]:
        return self._user

    def add_user(self, name: str, age: int) -> List[User]:
        self._user.append(User(name, age))
        return self._user


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # models
    user_model = UserModel()

    # window
    window = UserManagerWindow(user_model)
    window.show()

    sys.exit(app.exec())
