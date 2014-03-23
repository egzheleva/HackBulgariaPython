import unittest

import solution


class TestGenerateNumbers(unittest.TestCase):
    def test_numbers(self):
        solution.generate_numbers('text_file.txt', 100)

        with open('text_file.txt') as file:
            self.assertEqual(len(file.read().split()), 100)


if __name__ == '__main__':
    unittest.main()