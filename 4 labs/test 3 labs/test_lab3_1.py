import unittest
from typing import Callable

class TestGetNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.func = self._buildTestedFunction()
    @staticmethod
    def _buildTestedFunction() -> Callable[[list[int], list[int]], list[int]]:
        from lab_3 import get_numbers_in_between
        return get_numbers_in_between

    def test_2_4_32_16_96(self):
        a = [2, 4]
        b = [32, 16, 96]

        expected_numbers = [4, 8, 16]

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)


    def test_6_3_24_36(self):
        a = [6, 2]
        b = [24, 36]

        expected_numbers = [6, 12]

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)


    def test_3_4_24_48(self):
        a = [3, 4]
        b = [24, 48]

        expected_numbers = [12, 24]

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)

    def test_single_element_in_a(self):
        a = [3]
        b = [9, 12]

        expected_numbers = [3]

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)

    def test_large_range(self):
        a = [2, 5]
        b = [100, 200]

        expected_numbers = [10, 20, 50, 100]

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)

    def test_no_common_numbers(self):
        a = [7, 11]
        b = [30, 50]

        expected_numbers = []

        actual_numbers = self.func(a, b)

        self.assertEqual(expected_numbers, actual_numbers)

