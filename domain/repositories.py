import abc

from domain.entities import AccountType, Account, Statement


class AccountTypeAbstractModel(abc.ABC):
    @abc.abstractmethod
    def all(self) -> list[AccountType]:
        """
        すべての勘定科目タイプを返します。
        :return: 勘定科目タイプのリスト
        """
        pass


class AccountAbstractModel(abc.ABC):
    @abc.abstractmethod
    def all(self) -> list[Account]:
        """
        すべての勘定科目を返します。
        :return: 勘定科目のリスト
        """
        pass

    @abc.abstractmethod
    def update_account(self, account_id: int, account: Account):
        """
        account_id で指定した勘定科目の情報を更新します。
        :param account_id: 勘定科目ID
        :param account: 更新したい勘定科目の情報
        :return: None
        """
        pass


class StatementAbstractModel(abc.ABC):
    @abc.abstractmethod
    def get(self, year: int, month: int, day: int, account: Account or None) -> list[Statement]:
        """
        すべての明細の中から、年、月、日、勘定科目を絞り込み条件として取得します。
        指定しない場合、すべてを取得します。
        :param year: 年
        :param month: 月
        :param day: 日
        :param account: 勘定科目
        :return: 明細
        """
        pass

    @abc.abstractmethod
    def insert(self, statement: Statement):
        """
        新たな明細を追加します
        :param statement: 追加する明細
        :return: None
        """
        pass

    @abc.abstractmethod
    def get_daily_account_summary(self, year: int, month: int, day: int) -> list[Statement]:
        """
        引数で指定した年・月・日の、勘定科目ごとの合計金額を取得します。
        :param year: 年
        :param month: 月
        :param day: 日
        :return: 明細
        """
        pass

    @abc.abstractmethod
    def get_monthly_account_summary(self, year: int, month: int) -> list[Statement]:
        """
        引数で指定した年・月の、勘定科目ごとの合計金額を取得します。
        0件の場合は空の明細リストを返します。
        :param year: 年
        :param month: 月
        :return: 明細
        """
        pass

    @abc.abstractmethod
    def get_details_summary_by_accounts(self, year: int, month: int, account: Account) -> list[Statement]:
        """
        引数で指定した年・月・勘定科目の、日別の合計金額を取得します。
        :param year: 年
        :param month: 月
        :param account: 勘定科目
        :return: 明細
        """
        pass
