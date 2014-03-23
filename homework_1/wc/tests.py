import unittest

import solution


class TestWc(unittest.TestCase):
    def setUp(self):
        self.text = ('lqlqlq lq \n' + 'lqlq\n' + ' lq.')

        with open('text_file.txt', 'w') as file:
            file.write(self.text)

    def test_with_chars_command(self):
        self.assertEqual(solution.wc('chars', 'text_file.txt'),
                         109)

    def test_with_words_command(self):
        self.assertEqual(solution.wc('words', 'text_file.txt'), 20)

    def test_with_lines_command(self):
        self.assertEqual(solution.wc('lines', 'text_file.txt'), 3)

if __name__ == '__main__':
    unittest.main()