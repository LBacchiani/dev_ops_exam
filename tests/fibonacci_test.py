# Copyright (c) 2023 Lorenzo Bacchiani
# All rights reserved.

import unittest
from my_fibonacci import fibonacci

class FibonacciTestCase(unittest.TestCase):

    def test_fibonacci_sequence(self):
        # Test the first 10 numbers in the Fibonacci sequence
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        calculated_sequence = fibonacci(10)
        self.assertEqual(calculated_sequence, expected_sequence)

    def test_fibonacci_zero(self):
        # Test the Fibonacci sequence for n = 0
        expected_sequence = []
        calculated_sequence = fibonacci(0)
        self.assertEqual(calculated_sequence, expected_sequence)

    def test_fibonacci_negative(self):
        # Test the Fibonacci sequence for negative n
        expected_sequence = []
        calculated_sequence = fibonacci(-5)
        self.assertEqual(calculated_sequence, expected_sequence)


if __name__ == '__main__':
    unittest.main()
