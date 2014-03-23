import unittest

import solution


class TestCat2(unittest.TestCase):
    def setUp(self):
        self.text1 = 'lqlq lq'
        self.text2 = "I dont know what to say"
        self.text3 = "Python's great!"
        self.filenames = ['test_text_file1.txt', 'test_text_file2.txt',
                          'test_text_file3.txt']

        with open('test_text_file1.txt', 'w') as file:
            file.write(self.text1)

        with open('test_text_file2.txt', 'w') as file:
            file.write(self.text2)

        with open('test_text_file3.txt', 'w') as file:
            file.write(self.text3)

    def test_with_a_single_file(self):
        self.assertEqual(solution.cat2('test_text_file1.txt'), self.text1)

    def test_with_three_files(self):
        self.assertEqual(solution.cat2(*self.filenames),
                         '\n'.join([self.text1, self.text2, self.text3]))


if __name__ == '__main__':
    unittest.main()