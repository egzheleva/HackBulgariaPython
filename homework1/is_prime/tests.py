import unittest
from solution import is_prime


class IsPrimeTest(unittest.TestCase):
    def testing_is_prime_1(self):
        self.assertFalse(is_prime(1))

    def testing_is_prime_2(self):
        self.assertTrue(is_prime(2))

    def testing_is_prime_8(self):
        self.assertFalse(is_prime(8))

    def testing_is_prime_11(self):
        self.assertTrue(is_prime(11))

    def testing_is_prime_negative(self):
        self.assertFalse(is_prime(-10))
if __name__ == '__main__':
    unittest.main()

