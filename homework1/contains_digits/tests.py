import unittest
from solution import contains_digits


class ContainsDigitsTest(unittest.TestCase):
    def testing_contains_digits1(self):
        self.assertTrue(contains_digits(402123, [0, 3, 4]))

    def testing_contains_in_two_digit_number(self):
        self.assertFalse(contains_digits(666, [6, 4]))

    def testing_contains_in_four_number(self):
        self.assertFalse(contains_digits(123456789, [1,2,3,0]))

    def testin_contains_in_big_number(self):
        self.assertTrue(contains_digits(456, []))

if __name__ == '__main__':
       unittest.main()   