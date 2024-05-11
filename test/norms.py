import unittest

from src.norms import *


class NormTest(unittest.TestCase):
    def test_norm(self):
        matrix = [[-4, -3, -2],
                  [-1, 0, 1],
                  [2, 3, 4]]

        self.assertEqual(7.745966692414834, get_norm(matrix, Frobenius))
        self.assertEqual(9, get_norm(matrix, Inf))
        self.assertEqual(2, get_norm(matrix, MinusInf))
