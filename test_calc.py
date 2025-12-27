import unittest
from calc import add, subtract, multiply, safe_divide


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_safe_divide_normal(self):
        self.assertAlmostEqual(safe_divide(10, 4), 2.5)

    def test_safe_divide_zero(self):
        with self.assertRaises(ValueError):
            safe_divide(1, 0)


if __name__ == "__main__":
    unittest.main()
