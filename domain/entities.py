from domain.valueobjects import StatementCreatedAt, Amount


class AccountType(object):
    def __init__(self, type_id: int, type_name: str):
        self._type_id = type_id
        self._type_name = type_name

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


class Account(object):
    def __init__(self, account_id: int, account_name: str, account_type: AccountType,
                 default_amount: Amount or None = None):
        self._account_id = account_id
        self._account_name = account_name
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
        return hash(f"{self.id}:{self.name}:{self.type}")

    @property
    def id(self) -> int:
        return self._account_id

    @property
    def name(self) -> str:
        return self._account_name

    @property
    def type(self) -> AccountType:
        return self._account_type

    @property
    def default_amount(self) -> Amount:
        return self._default_amount


class Statement(object):
    def __init__(self, month: int, day: int, account_id: int, amount: Amount, created_at: StatementCreatedAt or None = None):
        self._month = month
        self._day = day
        self._account_id = account_id
        self._amount = amount
        self._created_at = created_at

    def __str__(self):
        s = f"""\
{self.account.name}:{self.month}月{self.day}日[{self.account.type.name}]({self._account_id}): \
{self.amount.value}円 @ {self.created_at.standard_format}     
"""
        return s

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
    def account(self) -> Account:
        if self._account_id == Accounts.Shiire.id:
            return Accounts.Shiire
        if self._account_id == Accounts.Settai.id:
            return Accounts.Settai
        if self._account_id == Accounts.Uriage.id:
            return Accounts.Uriage
        if self._account_id == Accounts.Oshibori.id:
            return Accounts.Oshibori

    @property
    def amount(self) -> Amount:
        return self._amount

    @property
    def created_at(self) -> StatementCreatedAt:
        return self._created_at


class AccountTypes(object):
    VariableCost = AccountType(1, "変動費")
    FixedCost = AccountType(2, "固定費")
    Sales = AccountType(3, "売上")

    @classmethod
    def get_instance_by_name(cls, name: str) -> AccountType:
        for var_name, instance in cls.__dict__.items():
            if isinstance(instance, AccountType) and instance.name == name:
                return instance


class Accounts(object):
    Shiire = Account(1, "仕入", AccountTypes.VariableCost)
    Settai = Account(2, "接待", AccountTypes.VariableCost)
    Zappi = Account(3, "雑費", AccountTypes.VariableCost)
    Shomohin = Account(4, "消耗品", AccountTypes.VariableCost)
    Yachin = Account(5, "家賃", AccountTypes.VariableCost)
    Aisu = Account(6, "アイス", AccountTypes.VariableCost)
    Osakagas = Account(7, "大阪ガス", AccountTypes.VariableCost)
    Hoken = Account(8, "保険", AccountTypes.VariableCost)
    Tsushinhi = Account(9, "通信費", AccountTypes.VariableCost)
    Shuzenhi = Account(10, "修繕費", AccountTypes.VariableCost)
    Kokokuhi = Account(11, "広告費", AccountTypes.VariableCost)
    Jidoshazei = Account(12, "自動車税", AccountTypes.VariableCost)
    Sakadai = Account(13, "酒代", AccountTypes.VariableCost)
    Bihin = Account(14, "備品", AccountTypes.VariableCost)

    Oshibori = Account(15, "おしぼり", AccountTypes.FixedCost, Amount(8800))
    Kujoki = Account(16, "駆除器", AccountTypes.FixedCost, Amount(0))
    Risueki = Account(17, "リース植木", AccountTypes.FixedCost, Amount(0))
    Chosakuken = Account(18, "著作権", AccountTypes.FixedCost, Amount(0))
    Karaoke = Account(19, "カラオケ", AccountTypes.FixedCost, Amount(0))

    Uriage = Account(20, "売上", AccountTypes.Sales)

    @classmethod
    def get_instance_by_name(cls, name: str) -> Account:
        for var_name, instance in cls.__dict__.items():
            if isinstance(instance, Account) and instance.name == name:
                return instance

    @classmethod
    def get_instance_by_hepburn(cls, hepburn: str) -> Account:
        print(cls.__dict__)
        for name, obj in cls.__dict__.items():
            if not isinstance(obj, Account):
                continue
            if hepburn == name.lower():
                return obj
