class InvalidConfigException(Exception):
    """
    アプリの設定情報に不備がある場合に送出されます。
    """
    pass


class InvalidAmountException(Exception):
    """
    金額入力欄に不適切な値があった場合に送出されます。
    """
    pass


class AccountTypeNotFoundException(Exception):
    """
    存在しない勘定科目タイプへのアクセスで送出されます。
    """
    pass


class AccountNotFoundException(Exception):
    """
    存在しない勘定科目へのアクセスで送出されます。
    """
