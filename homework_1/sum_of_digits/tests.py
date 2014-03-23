from solution import sum_of_digits
import unittest


class SumOfDigitsTest(unittest.TestCase):
	def test_sum_of_digits(self):
		self.assertEqual(6, sum_of_digits(123))
	def test_sum(self):
		self.assertEqual(6, sum_of_digits(6))
	def test_negative_number(self):
		self.assertEqual(1, sum_of_digits(-10))


if __name__ == '__main__':
	unittest.main()