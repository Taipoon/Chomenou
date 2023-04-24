from domain.valueobjects import Amount


class UpsertAccountCriteria(object):
    def __init__(self, account_name: str = None, account_name_hepburn: str = None,
                 account_type_id: int = None, default_amount: Amount = None):
        self._account_name = account_name
        self._account_name_hepburn = account_name_hepburn
        self._account_type_id = account_type_id
        self._default_amount = default_amount

    @property
    def name(self) -> str:
        return self._account_name

    @property
    def name_hepburn(self) -> str:
        return self._account_name_hepburn

    @property
    def type_id(self) -> int:
        return self._account_type_id

    @property
    def default_amount(self) -> Amount:
        return self._default_amount
