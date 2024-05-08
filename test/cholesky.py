from src.cholesky import *
import unittest

class CholeskyTest(unittest.TestCase):

    def test_cholesky(self):
        A = [
            [4, 2, 1, 1],
            [2, 5, 0, 3],
            [1, 0, 7, 2],
            [1, 3, 2, 8]
        ]
        sol = cholesky(A)
        expected = [
            [2., 1., 0.5, 0.5],
            [0., 2., -0.25, 1.25],
            [0., 0., 2.5860201081971503, 0.7975576034626725],
            [0., 0., 0., 2.3561413092509707]
        ]

        for vec_1, vec_2 in zip(sol, expected):
            for x, y in zip(vec_1, vec_2):
                self.assertEqual(x, y)
