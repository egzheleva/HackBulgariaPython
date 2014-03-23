import unittest
from solution import contains_digit


class ContainsDigitTest(unittest.TestCase):
    def testing_contains_in_three_digit_number(self):
        self.assertFalse(contains_digit(123, 4))

    def testing_contains_in_two_digit_number(self):
        self.assertTrue(contains_digit(42, 2))

    def testing_contains_in_four_number(self):
        self.assertTrue(contains_digit(1000, 0))

    def testin_contains_in_big_number(self):
        self.assertFalse(contains_digit(12346789, 5))

if __name__ == '__main__':
       unittest.main()   