# Copyright (c) 2023 Lorenzo Bacchiani
# All rights reserved.

import unittest
from prime_numbers import prime_numbers

class TestPrimeNumbers(unittest.TestCase):

    def test_prime_numbers(self):
        result = prime_numbers(20)
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()