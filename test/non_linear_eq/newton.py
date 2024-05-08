import unittest
from src.non_linear_eq.newton import *


class NewtonTest(unittest.TestCase):
    def test_newton_non_linear(self):
        A = [lambda x: (1.4 * x[0]) - x[1], lambda x: (x[0] ** 2) - (1.6 * x[0]) - x[1]]
        b = [0.6, 4.6]
        sol = newton_non_linear(A, b, 0.0001, [5.0, 5.0])
        expected = [4.000002976873368, 5.000004167622031]

        for a, b in zip(sol, expected):
            self.assertEqual(a, b)
