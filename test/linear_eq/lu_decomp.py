import unittest
import numpy as np

from src.constants import DEFAULT_DELTA
from src.linear_eq.lu_decomp import lu_decomp, solve, solve_upper_triangular


class LuDecompTest(unittest.TestCase):
    def test_differentiate_linear(self):
        matrix = [
            [1, 2.2, 1],
            [13.44, 4, 1.12],
            [0.001, 2, -1]
        ]

        p, l, u = lu_decomp(matrix)
        mult = p @ l @ u

        for i in range(0, 3):
            for j in range(0, 3):
                self.assertTrue(abs(matrix[i][j] - mult[i][j]) < DEFAULT_DELTA)

    def test_solve_upper(self):
        matrix = [
            [3, 3, 5],
            [0, 1, -12],
            [0, 0, 3],
        ]

        sol = solve_upper_triangular(matrix, [26, -49, 12])
        expected = np.array([3.0, -1.0, 4.0])

        for i in range(0, len(sol)):
            self.assertEqual(sol[i], expected[i])

    def test_solve_upper_with_normal(self):
        # Try to solve a matrix that is already Upper
        matrix = [
            [3, 3, 5],
            [0, 1, -12],
            [0, 0, 3],
        ]

        sol = solve(matrix, [26, -49, 12])
        expected = np.array([3.0, -1.0, 4.0])

        for i in range(0, len(sol)):
            self.assertEqual(sol[i], expected[i])

    def test_solve_matrix(self):
        # Try to solve a matrix that is not Upper/Lower
        matrix = [
            [3, 3, 5],
            [1, 1, -12],
            [0, -4, 3],
        ]

        sol = solve(matrix, [26, -46, 16])
        expected = np.array([3.0, -1.0, 4.0])

        for i in range(0, len(sol)):
            self.assertTrue((sol[i] - expected[i]) < DEFAULT_DELTA)
