import unittest
from solution import is_int_palindrome


class IsIntPalindromeTest(unittest.TestCase):
    def testing_is_palindrome_one_digit_int(self):
        self.assertTrue(is_int_palindrome(100001))

    def testing_is_palindrome_two_digit_int(self):
        self.assertFalse(is_int_palindrome(42))

    def testing_is_palindrome_big_number(self):
        self.assertTrue(is_int_palindrome(100001))

    def testing_is_palindrome_three_equal_digit_int(self):
        self.assertTrue(is_int_palindrome(999))

    def testing_is_palindrome_three_digit_int(self):
        self.assertFalse(is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()