from domain.valueobjects import Amount, StatementCreatedAt


class AccountType(object):
    def __init__(self, type_id: int, type_name: str, type_name_hepburn: str):
        self._type_id = type_id
        self._type_name = type_name
        self._type_name_hepburn = type_name_hepburn

    def __eq__(self, other):
        if not isinstance(other, AccountType):
            return False
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.name}({self.id})"

    @property
    def id(self) -> int:
        return self._type_id

    @property
    def name(self) -> str:
        return self._type_name

    @property
    def name_hepburn(self) -> str:
        return self._type_name_hepburn


class Account(object):
    def __init__(self, account_id: int, account_name: str, account_name_hepburn: str,
                 account_type: AccountType, default_amount: Amount or None = None):
        self._account_id = account_id
        self._account_name = account_name
        self._account_name_hepburn = account_name_hepburn
        self._account_type = account_type
        self._default_amount = default_amount or Amount(0)

    def __eq__(self, other):
        if not isinstance(other, Account):
            return False
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self._account_name

    def __hash__(self):
        return hash(f"{self._account_id}:{self._account_name}:{self._account_type}")

    @property
    def id(self) -> int:
        return self._account_id

    @property
    def name(self) -> str:
        return self._account_name

    @property
    def name_hepburn(self) -> str:
        return self._account_name_hepburn

    @property
    def type(self) -> AccountType:
        return self._account_type

    @property
    def default_amount(self) -> Amount:
        return self._default_amount


class Statement(object):
    def __init__(self, year: int, month: int, day: int, account_id: int,
                 amount: Amount, created_at: StatementCreatedAt or None = None):
        self._year = year
        self._month = month
        self._day = day
        self._account_id = account_id
        self._amount = amount
        self._created_at = created_at

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @property
    def display_date(self) -> str:
        return f"{self.month}月 {self.day}日"

    @property
    def account_id(self) -> int:
        return self._account_id

    @property
    def amount(self) -> Amount:
        return self._amount

    @property
    def created_at(self) -> StatementCreatedAt or None:
        if self._created_at is None:
            return None
        return self._created_at


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
