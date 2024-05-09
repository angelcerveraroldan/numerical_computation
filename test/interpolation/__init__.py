import unittest, math
import numpy as np

from src.interpolation import *

x = np.array([25, 50, 75])
fx = np.array([829800, 3298250, 7405450])


class TestInterpolation(unittest.TestCase):
    def test_vandermonde(self):
        vander = vandermonde(x, fx)
        expected = np.array([1311., 413., 100.])
        for i in range(len(vander)):
            self.assertAlmostEqual(vander[i], expected[i])

    def test_lagrangian(self):
        lagrange = lagrangian(x, fx)
        expected = np.poly1d([1311, 413, 100])
        self.assertEqual(lagrange, expected)

    def test_newton_polynomial(self):
        newton = newton_polynomial(x, fx, 0)
        expected = 100
        self.assertEqual(newton, expected)
        newton = newton_polynomial(x, fx, 1)
        expected = 1824
        self.assertEqual(newton, expected)