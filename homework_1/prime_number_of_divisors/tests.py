import unittest
from solution import prime_number_of_divisors


class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def testing_prime_num_of_div_7(self):
        self.assertTrue(prime_number_of_divisors(7))
    def testing_prime_num_of_div_8(self):
        self.assertFalse(prime_number_of_divisors(8))
    def testing_prime_num_of_div_9(self):
        self.assertTrue(prime_number_of_divisors(9))

if __name__ == '__main__':
      unittest.main()  
        