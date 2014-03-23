import unittest

import solution


class TestCat(unittest.TestCase):
    def setUp(self):
        self.text = 'lqlq lq'

        with open('text_file.txt', 'w') as file:
            file.write(self.text)

    def test_with_text_file(self):
        self.assertEqual(solution.cat('text_file.txt'), self.text)


if __name__ == '__main__':
    unittest.main()
