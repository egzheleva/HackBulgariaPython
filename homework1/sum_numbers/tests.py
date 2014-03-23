import unittest

import solution


class TestSumNumbers(unittest.TestCase):
    def test_with_5_numbers(self):
        with open('test_file_with_numbers.txt', 'w') as file:
            file.write(' '.join(map(str, range(6))))

        self.assertEqual(solution.sum_numbers('test_file_with_numbers.txt'),
                         sum(range(6)))


if __name__ == '__main__':
    unittest.main()