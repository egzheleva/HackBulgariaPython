import unittest
from solution import sevens_in_a_row


class SevensInARoqTest(unittest.TestCase):
    def testing_sevens_in_a_row1(self):
        self.assertTrue(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))

    def testing_sevens_in_a_row2(self):
        self.assertFalse(sevens_in_a_row([1, 7, 1, 7, 7], 4))  

    def testing_sevens_in_a_row3(self):
        self.assertTrue(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))

    def testing_sevens_in_a_row4(self):
        self.assertTrue(sevens_in_a_row([7, 2, 1, 6, 2], 1))

if __name__ == '__main__':
    unittest.main()



        