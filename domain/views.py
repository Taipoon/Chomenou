import abc

from domain.entities import Statement, Account, MonthlyAccountSummary
from domain.valueobjects import Amount


class AbstractBaseView(abc.ABC):
    @abc.abstractmethod
    def initialize_ui(self):
        """
        View の初期化を行います
        :return: None
        """
        pass


class MainView(AbstractBaseView):
    @abc.abstractmethod
    def update_selected_account(self, account: Account):
        """
        選択中の勘定科目の表示を変更する
        :param account: 勘定科目
        :return: None
        """
        pass

    @abc.abstractmethod
    def update_date_input_viewer(self, y: int, m: int, d: int):
        """
        日付入力欄を引数で与えられた年月日に更新します
        :param y: 年
        :param m: 月
        :param d: 日
        :return: None
        """
        pass

    @abc.abstractmethod
    def update_calender_viewer(self, y: int, m: int, d: int):
        """
        カレンダーの選択月日を引数で与えられた年月日に変更します
        :param y: 年
        :param m: 月
        :param d: 日
        :return: None
        """
        pass

    @abc.abstractmethod
    def clear_amount_entry_field(self):
        """
        金額入力欄をリセットします
        :return: None
        """
        pass

    @abc.abstractmethod
    def set_amount_entry_field(self, value: int):
        """
        金額入力欄に値をセットします
        :param value: 値
        :return: None
        """

    @abc.abstractmethod
    def update_daily_summary_viewer(self, statements: list[Statement]):
        """
        日ごとのサマリを表示します
        :param statements: 明細
        :return:
        """
        pass

    @abc.abstractmethod
    def update_monthly_summary_viewer(self, summary: list[MonthlyAccountSummary]):
        """
        月ごとのサマリを表示します
        :param summary:
        :return:
        """
        pass


class AccountsEditorView(AbstractBaseView):
    @abc.abstractmethod
    def update_line_edit(self, account: Account, amount: Amount):
        """
        指定したアカウントの初期金額欄を更新します
        :param account: 更新したいアカウント
        :param amount: 更新する値
        :return: None
        """
        pass


class BulkInsertionView(AbstractBaseView):
    @abc.abstractmethod
    def update_line_edit(self, value: int):
        """
        一斉記帳する金額の入力欄を更新します
        :param value: 金額
        :return: None
        """
        pass
