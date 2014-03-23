import unittest
from solution import count_substrings


class CountSubstringsTest(unittest.TestCase):
    def testing_count_substring1(self):
        self.assertEqual(2, count_substrings("This is a test string", "is"))
    def testing_count_substring2(self):
        self.assertEqual(2, count_substrings("bababa", "baba"))
    def testing_count_substring3(self):
        self.assertEqual(4, count_substrings("Python is an awesome language to program in!", "0"))
    def testing_count_substring4(self):
        self.assertEqual(0, count_substrings("We have nothing in common!", "really?"))
    def testing_count_substring5(self):
        self.assertEqual(2, count_substrings("This is this and that is this", "this"))

if __name__ == '__main__':
    unittest.main()