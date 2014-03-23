import unittest
from solution import is_number_balanced


class IsNumberBalancedTest(unittest.TestCase):
    def testing_is_number_balanced1(self):
        self.assertTrue(is_number_balanced(9))

    def testing_is_number_balanced2(self):
        self.assertTrue(is_number_balanced(11))

    def testing_is_number_balanced3(self):
        self.assertFalse(is_number_balanced(13))

    def testing_is_number_balanced4(self):
        self.assertTrue(is_number_balanced(121))

    def testing_is_number_balanced5(self):
        self.assertTrue(is_number_balanced(4518))

    def testing_is_number_balanced6(self):
        self.assertFalse(is_number_balanced(28471))

    def testing_is_number_balanced7(self):
        self.assertTrue(is_number_balanced(1238033))

if __name__ == '__main__':
    unittest.main()
