import unittest
from solution import sum_of_divisors


class SumOfDivisorsTest(unittest.TestCase):
    def testing_sum_of_divisors_8(self):
        self.assertEqual(15, sum_of_divisors(8))

    def testing_sum_of_divisors_7(self):
        self.assertEqual(8, sum_of_divisors(7))

    def testing_sum_of_divisors_1(self):
        self.assertEqual(1, sum_of_divisors(1))

    def testing_sum_of_divisors_1000(self):
        self.assertEqual(2340, sum_of_divisors(1000))

if __name__ == '__main__':
    unittest.main()
    