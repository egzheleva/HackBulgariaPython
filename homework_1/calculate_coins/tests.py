import unittest
from solution import calculate_coins


class CalculateCoinsTest(unittest.TestCase):
    """testing calculate_coins"""
    def test_one(self):
        self.assertEqual({1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}, calculate_coins(0.53))

    def test_two(self):
        self.assertEqual({1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}, calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()
