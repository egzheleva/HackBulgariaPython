import unittest
from solution import count_vowels


class CountVowelsTest(unittest.TestCase):
    def testing_count_vowels1(self):
        self.assertEqual(2, count_vowels("Python"))

    def testing_count_vowels2(self):
        self.assertEqual(8, count_vowels("Theistareykjarbunga"))

    def testing_count_vowels3(self):
        self.assertEqual(0, count_vowels("grrrrgh!"))

    def testing_count_vowels4(self):
        self.assertEqual(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def testing_count_vowels5(self):
        self.assertEqual(8, count_vowels("A nice day to code!")) 

if __name__ == '__main__':
    unittest.main()