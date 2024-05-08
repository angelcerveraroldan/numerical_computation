import unittest

from src.matrix import add_rows, pivot, row_swap, scalar_row, sub_rows, add_rows_scalar


class MatrixOpsTest(unittest.TestCase):
    def test_add_sub_rows(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual([4, 6], add_rows(matrix, 0, 1))
        self.assertEqual([2, 2], sub_rows(matrix, 1, 0))

    def test_add_rows_scalar(self):
        matrix = [[2.3, 3.4], [1, 2]]
        sol = add_rows_scalar(matrix, 1, 0, -2)
        expected = [[2.3, 3.4], [-3.5999999999999996, -4.8]]
        for r_1, r_2 in zip(sol, expected):
            for a, b in zip(r_1,r_2):
                self.assertEqual(a, b)

    def test_swap_rows(self):
        matrix = [[1, 2], [3, 4]]
        expect = [[3, 4], [1, 2]]
        row_swap(matrix, 0, 1)

        self.assertEqual(expect, matrix)

    def test_multiply_row(self):
        matrix = [[1, 2], [3, 4]]
        scalar_row(matrix, 0, 2)
        self.assertEqual(matrix[0], [2, 4])

    def test_pivot(self):
        matrix = [
            [1, 0, 2],
            [3, 0, 4],
            [3, 4, 1],
        ]

        expected = [
            [1, 0, 2],
            [3, 4, 1],
            [3, 0, 4],
        ]

        pivot(matrix, 1)
        self.assertEqual(expected, matrix)
