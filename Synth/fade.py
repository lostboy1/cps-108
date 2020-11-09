# Put your code here:



# Keep working until you pass all these tests
# (run them by pressing F5):

from unittest import TestCase, main

class Tests(TestCase):
    def test_fade_function_exists(self):
        assert callable(fade)

    def test_simple_fade(self):
        self.assertEqual(
            fade([50,50,50,50,50], 5),
            [50,40,30,20,10],
        )

    def test_short_fade(self):
        self.assertEqual(
            fade([50,50], 2),
            [50,25],
        )

    def test_fade_ends_with_zeros(self):
        self.assertEqual(
            fade([30,30,30,30,30,30], 3),
            [30,20,10,0,0,0],
        )

if __name__ == '__main__':
    main(exit=False, failfast=True, verbosity=2)
