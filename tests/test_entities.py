import unittest

from domain.entities import AccountType


class TestAccountType(unittest.TestCase):
    def test_property(self):
        at = AccountType(type_id=1, type_name="仕入", type_name_hepburn="shiire")
        self.assertEqual(1, at.id)
        self.assertEqual("仕入", at.name)
        self.assertEqual("shiire", at.name_hepburn)

    def test_eq(self):
        with self.subTest("type_id が同じ場合に等価演算子でTrueを返せる"):
            at1 = AccountType(type_id=1, type_name="仕入", type_name_hepburn="shiire")
            at2 = AccountType(type_id=1, type_name="接待", type_name_hepburn="settai")
            self.assertTrue(at1 == at2)

        with self.subTest("type_id が異なる場合に等価演算子でFalseを返せる"):
            at1 = AccountType(type_id=1, type_name="仕入", type_name_hepburn="shiire")
            at2 = AccountType(type_id=2, type_name="仕入", type_name_hepburn="shiire")
            self.assertFalse(at1 == at2)

    def test_ne(self):
        with self.subTest("type_id が異なる場合に非等価演算子でTrueを返せる"):
            at1 = AccountType(type_id=1, type_name="仕入", type_name_hepburn="shiire")
            at2 = AccountType(type_id=2, type_name="仕入", type_name_hepburn="shiire")
            self.assertTrue(at1 != at2)

        with self.subTest("type_id が同じ場合に非等価演算子でFalseを返せる"):
            at1 = AccountType(type_id=2, type_name="仕入", type_name_hepburn="shiire")
            at2 = AccountType(type_id=2, type_name="接待", type_name_hepburn="settai")
            self.assertFalse(at1 != at2)


class TestAccount(unittest.TestCase):
    pass


class TestStatement(unittest.TestCase):
    def test_eq(self):
        # TODO: 実装
        pass


if __name__ == '__main__':
    unittest.main()
