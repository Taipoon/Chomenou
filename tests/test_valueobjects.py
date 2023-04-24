import unittest

from domain.exceptions import InvalidAmountException
from domain.valueobjects import Amount


# noinspection NonAsciiCharacters
class TestAmount(unittest.TestCase):
    def test_イコールで正しく評価できる(self):
        with self.subTest("等しい場合に等価演算子でTrueを返せる"):
            a1 = Amount(5000)
            a2 = Amount(5000)
            self.assertTrue(a1 == a2)

        with self.subTest("等しくない場合に等価演算子でFalseを返せる"):
            a1 = Amount(3000)
            a2 = Amount(3001)
            self.assertFalse(a1 == a2)

    def test_ノットイコールで正しく評価できる(self):
        with self.subTest("等しくない場合に非等価演算子でTrueを返せる"):
            a1 = Amount(3000)
            a2 = Amount(3001)
            self.assertTrue(a1 != a2)

        with self.subTest("等しい場合に非等価演算子でFalseを返せる"):
            a1 = Amount(3000)
            a2 = Amount(3000)
            self.assertFalse(a1 != a2)

    def test_valueプロパティの値(self):
        a = Amount(0)
        self.assertEqual(0, a.value)

    def test_value_with_unitプロパティの値(self):
        a = Amount(2500)
        self.assertEqual("2500円", a.value_with_unit)

    def test_comma_value_with_unitプロパティの値(self):
        with self.subTest("3桁以下の場合はカンマを付けずに単位をつけて値を返せる"):
            a = Amount(100)
            self.assertEqual("100円", a.comma_value_with_unit)

        with self.subTest("4桁以上の場合にカンマと単位をつけて値を返せる"):
            a = Amount(3580)
            self.assertEqual("3,580円", a.comma_value_with_unit)

        with self.subTest("多くの桁を持っている場合も、適切にカンマと単位をつけて値を返せる"):
            a = Amount(123456789)
            self.assertEqual("123,456,789円", a.comma_value_with_unit)

    def test_金額として不適切な値をコンストラクタに与えてInvalidAmountExceptionを送出できる(self):
        with self.assertRaises(InvalidAmountException):
            a = Amount(-1)


if __name__ == '__main__':
    unittest.main()
