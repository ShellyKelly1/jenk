import unittest
from src.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 6), 8)



if __name__ == '__main__':
    unittest.main()
