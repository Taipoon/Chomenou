import abc

from domain.entities import AccountType, Account, Statement


class IAccountTypeRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> list[AccountType]:
        """
        すべての勘定科目タイプを取得します。
        結果は勘定科目タイプIDで昇順ソートされています。
        結果が0件の場合は空のリストを返します。
        :return: 勘定科目タイプのリスト
        """
        raise NotImplementedError


class IAccountRepository(abc.ABC):
    @abc.abstractmethod
    def all(self) -> list[Account]:
        """
        すべての勘定科目を返します。
        結果は勘定科目IDで昇順ソートされています。
        結果が0件の場合は空のリストを返します。
        :return: 勘定科目のリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_id(self, account_id: int) -> Account:
        """
        引数で指定した id を持つ勘定科目を返します。
        存在しない場合は AccountNotFoundException が送出されます。
        :param account_id: 勘定科目ID
        :return: 勘定科目
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update_account(self, account_id: int, new_account: Account):
        """
        account_id で指定した勘定科目の情報を更新します。
        :param account_id: 勘定科目ID
        :param new_account: 更新する勘定科目の情報
        :return: None
        """
        raise NotImplementedError


class IStatementRepository(abc.ABC):
    @abc.abstractmethod
    def get_all_years(self) -> list[int]:
        """
        記帳データが1件以上存在するすべての年度を取得します。
        結果は昇順でソートされています。
        結果が0件の場合は空のリストを返します。
        :return: 年度を要素に持つリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, year: int or None = None, month: int or None = None,
            day: int or None = None, account_id: int or None = None) -> list[Statement]:
        """
        すべての明細の中から、年・月・日・勘定科目IDを絞り込み条件として取得します。
        何も指定しない場合、すべてが対象になります。
        結果の順序は、年、月、日、勘定科目ID、作成日の順で、昇順ソートされます。
        結果が0件の場合は空のリストを返します。
        :param year: 年
        :param month: 月
        :param day: 日
        :param account_id: 勘定科目ID
        :return: 明細を要素に持つリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def insert(self, statement: Statement):
        """
        新たな明細を追加します。
        :param statement: 追加する明細
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_daily_account_summary(self, year: int, month: int, day: int) -> list[Statement]:
        """
        引数で指定した年・月・日の明細データを勘定科目ごとに集計して取得します。
        結果の明細は勘定科目IDで昇順ソートされています。
        0件の場合は空のリストを返します。
        :param year: 年
        :param month: 月
        :param day: 日
        :return: 明細のリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_monthly_account_summary(self, year: int, month: int) -> list[Statement]:
        """
        引数で指定した年・月の明細データを勘定科目ごとに集計して取得します。
        結果の明細は勘定科目IDで昇順ソートされています。
        0件の場合は空のリストを返します。
        :param year: 年
        :param month: 月
        :return: 明細のリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_yearly_account_summary(self, year: int) -> list[Statement]:
        """
        引数で指定した年の明細データを月別かつ勘定科目ごとに集計して取得します。
        結果の明細は月、勘定科目IDの順で昇順ソートされています。
        0件の場合は空のリストを返します。
        :param year: 年
        :return: 明細のリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_daily_total_by_account_and_month_and_year(self, year: int, month: int, account_id: int) -> list[Statement]:
        """
        引数で指定した年・月・勘定科目の明細データを日毎に集計して取得します。
        結果の明細は日で昇順ソートされています。
        0件の場合は空のリストを返します。
        :param year: 年
        :param month: 月
        :param account_id: 勘定科目ID
        :return: 明細のリスト
        """
        raise NotImplementedError
