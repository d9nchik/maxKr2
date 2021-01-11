from unittest import TestCase

import sorts


class Test(TestCase):
    def test_direct_merge(self):
        array = [8, 23, 5, 65, 44, 33, 1, 6, 297, 31, 89, 0, 165, 44, 23, 31, 56, 89, 27, 68, 43]
        self.assertEqual(sorts.direct_merge(array), sorted(array))

    def test_natural_merge(self):
        array = [8, 23, 5, 65, 44, 33, 1, 6, 297, 31, 89, 0, 165, 44, 23, 31, 56, 89, 27, 68, 43]
        self.assertEqual(sorts.natural_merge(array), sorted(array))

    def test_balanced_poly_path_merge(self):
        array = [8, 23, 5, 65, 44, 33, 1, 6, 297, 31, 89, 0, 165, 44, 23, 31, 56, 89, 27, 68, 43]
        self.assertEqual(sorts.balanced_poly_path_merge(array), sorted(array))

    def test_fibonacci_n(self):
        fibonacci4 = sorts.fibonacci_n(4)
        self.assertEqual(fibonacci4(11), 31)
        self.assertEqual(fibonacci4(1), 0)
    #
    # def test_print_ideal_division(self):
    #     self.fail()
