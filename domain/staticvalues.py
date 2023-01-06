"""
勘定科目一覧
"""
from domain.entities import Account, AccountType
from domain.value_objects import Amount


VariableCost = AccountType(1, "変動費")
FixedCost = AccountType(2, "固定費")
Sales = AccountType(3, "売上")


Shiire = Account(1, "仕入", VariableCost)
Settai = Account(2, "接待", VariableCost)
Uriage = Account(3, "売上", Sales)
Oshibori = Account(4, "おしぼり", FixedCost, Amount(8800))
