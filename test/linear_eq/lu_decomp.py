import unittest
import numpy as np

from src.constants import DEFAULT_DELTA
from src.linear_eq.lu_decomp import lu_decomp, solve, solve_upper_triangular, lu_decomp_no_pp


class LuDecompTest(unittest.TestCase):
    def decompose_matrix(self):
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

    def test_lu_decomp_no_pp(self):
        matrix = np.asfarray([
            [-3, 2, -1],
            [6, -6, 7],
            [3, -4, 4]
        ])
        l, u = lu_decomp_no_pp(matrix)
        l_e = [
            [1, 0, 0],
            [-2, 1, 0],
            [-1, 1, 1]
        ]
        u_e = [
            [-3, 2, -1],
            [0, -2, 5],
            [0, 0, -2]
        ]
        for r_1, r_2 in zip(l, l_e):
            for x, y in zip(r_1,r_2):
                self.assertEqual(x, y)

        for r_1, r_2 in zip(u, u_e):
            for x, y in zip(r_1,r_2):
                self.assertEqual(x, y)

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
