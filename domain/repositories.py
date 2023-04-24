import abc

from domain.aggregates import MonthlyStatementSummary, YearlyStatementSummary
from domain.criterias import UpsertAccountCriteria
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
    def find_by_account_type_id(self, account_type_id: int) -> list[Account]:
        """
        引数で指定した account_type_id を持つ勘定科目のリストを返します。
        結果は勘定科目IDで昇順ソートされています。
        存在しない場合は AccountNotFoundException が送出されます。
        :param account_type_id: 勘定科目タイプID
        :return: 勘定科目のリスト
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, account_id: int, update_account_criteria: UpsertAccountCriteria):
        """
        引数で渡された account_id の情報を update_account_criteria で更新します。
        account_id を持つ勘定科目が存在しない場合は AccountNotFoundException が送出されます。
        :param account_id: 勘定科目ID
        :param update_account_criteria: 勘定科目変更条件
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, new_account_criteria: UpsertAccountCriteria):
        """
        引数で渡された new_account_criteria の情報で勘定科目を新規に作成します。
        :param new_account_criteria: 勘定科目追加条件
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
    def upsert(self, statement: Statement):
        """
        新たな明細を追加または修正します。
        :param statement: 追加・修正する明細
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_monthly_statement_summary(self, year: int, month: int) -> MonthlyStatementSummary:
        """
        引数で指定した年・月の明細データを勘定科目ごとに集計して取得します。
        結果の明細は勘定科目IDで昇順ソートされています。
        :param year: 年
        :param month: 月
        :return: 月間明細サマリ
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_yearly_statement_summary(self, year: int) -> YearlyStatementSummary:
        """
        引数で指定した年の明細データを月別かつ勘定科目ごとに集計して取得します。
        結果の明細は月、勘定科目IDの順で昇順ソートされています。
        :param year: 年
        :return: 年間明細サマリ
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_monthly_statement_detail(self, year: int, month: int, account_id: int) -> list[Statement]:
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
