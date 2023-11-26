#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """
        Test case for the max_integer function.

        This test case checks the correctness of the max_integer function by
        asserting the expected output for different input scenarios.
        Inputs:
        - List of integers
        - List of negative integers
        - List of duplicate integers
        - List of strings
        Outputs:
        - Maximum integer value in the list
        - None if the list is empty or no arguments are provided
        - Maximum string value in the list
        Returns:
        - None
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 3]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")


if __name__ == '__main__':
    unittest.main()
