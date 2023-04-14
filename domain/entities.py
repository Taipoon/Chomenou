from domain.valueobjects import Amount


class AccountType(object):
    def __init__(self, type_id: int, type_name: str, type_name_hepburn: str):
        self._type_id = type_id
        self._type_name = type_name
        self._type_name_hepburn = type_name_hepburn

    def __eq__(self, other):
        if isinstance(other, AccountType):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.name}({self.id})"

    @property
    def id(self) -> int:
        """勘定科目種別ID"""
        return self._type_id

    @property
    def name(self) -> str:
        """勘定科目種別名"""
        return self._type_name

    @property
    def name_hepburn(self) -> str:
        """ヘボン表記 勘定科目種別名"""
        return self._type_name_hepburn


class Account(object):
    def __init__(self, account_id: int, account_name: str, account_name_hepburn: str,
                 account_type: AccountType, default_amount: Amount = Amount(0)):
        self._account_id = account_id
        self._account_name = account_name
        self._account_name_hepburn = account_name_hepburn
        self._account_type = account_type
        self._default_amount = default_amount

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self._account_name

    def __hash__(self):
        return hash(f"{self._account_id}:{self._account_name}:{self._account_type}")

    @property
    def id(self) -> int:
        """勘定科目ID"""
        return self._account_id

    @property
    def name(self) -> str:
        """勘定科目名"""
        return self._account_name

    @property
    def name_hepburn(self) -> str:
        """ヘボン表記 勘定科目名"""
        return self._account_name_hepburn

    @property
    def type(self) -> AccountType:
        """勘定科目種別"""
        return self._account_type

    @property
    def default_amount(self) -> Amount:
        """初期設定額"""
        return self._default_amount


class Statement(object):
    def __init__(self, year: int, month: int, day: int, account_id: int, amount: Amount):
        self._year = year
        self._month = month
        self._day = day

        account = Accounts().get_account_by_id(account_id)
        self._account_id = account.id

        self._amount = amount

    @property
    def year(self) -> int:
        """年"""
        return self._year

    @property
    def month(self) -> int:
        """月"""
        return self._month

    @property
    def day(self) -> int:
        """日"""
        return self._day

    @property
    def display_date(self) -> str:
        """日付 (書式: m月 d日)"""
        return f"{self.month}月 {self.day}日"

    @property
    def account_id(self) -> int:
        """勘定科目ID"""
        return self._account_id

    @property
    def amount(self) -> Amount:
        """金額"""
        return self._amount


class MonthlyAccountSummary(object):
    def __init__(self, account: Account, total_amount: Amount, details: list[Statement]):
        self._id = account.id
        self._account = account
        self._total_amount = total_amount
        self._details = details

    @property
    def id(self) -> int:
        return self._id

    @property
    def account(self):
        return self._account

    @property
    def details(self):
        return self._details

    @property
    def total_amount(self) -> Amount:
        return self._total_amount


class ExportDataTransferObject(object):
    # TODO: 集約として年度ごとの書き出すサマリオブジェクトを設計すること
    def __init__(self, year: int, month: int, account_name: str, total: Amount):
        self._year = year
        self._month = month
        self._account_name = account_name
        self._total = total
