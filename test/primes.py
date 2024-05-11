import unittest
from src.primes import *


class PrimesTest(unittest.TestCase):
    def test_first_hundred(self):
        real_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        primes = Primes(100)

        self.assertEqual(
            list(filter(lambda x: x < 100, real_primes)),
            primes.get_primes()
        )

        primes.find_next_n(5)

        self.assertEqual(primes.get_primes()[-5:], [101, 103, 107, 109, 113])

    def test_lots_of_primes(self):
        primes = Primes(1_000_000)
        self.assertEqual(len(primes.get_primes()), 78498)

        primes = Primes(10_000_000)
        self.assertEqual(len(primes.get_primes()), 664579)
