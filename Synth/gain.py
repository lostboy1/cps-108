# Put your code here:



# Keep working until you pass all these tests
# (run them by pressing F5):

from unittest import TestCase, main

class Tests(TestCase):
    def test_function_exists(self):
        assert callable(gain)

    def test_gain_of_10(self):
        self.assertEqual(gain([1, 2, 3], 10), [10, 20, 30])

    def test_gain_of_2(self):
        self.assertEqual(gain([1, 2, 3], 2), [2, 4, 6])

    def test_gain_of_0(self):
        self.assertEqual(gain([1, 2, 3], 0), [0, 0, 0])

    def test_gain_of_empty_list_4(self):
        self.assertEqual(gain([], 4), [])

    def test_gain_of_one_half(self):
        self.assertEqual(gain([10, 11, 12, 13], 0.5), [5, 5.5, 6, 6.5])

if __name__ == '__main__':
    main(exit=False, failfast=True, verbosity=2)
