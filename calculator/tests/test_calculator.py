import unittest
from src.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 6), 8)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)

    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == '__main__':
    unittest.main()
