import math
import unittest

from src.constants import DEFAULT_DELTA
from src.non_linear_eq.newton_nl import newton_method


class NewtonNonLinearTest(unittest.TestCase):
    def test_differentiate_linear(self):
        """
        The following matrix represents the equations:

        x0^2 + x1^2 = 4
        x0^2 - x1   = 4
        """

        A = [
            [lambda x: x[0], lambda x: x[1]],
            [lambda x: x[0], lambda x: -1],
        ]

        b = [4, 4]

        acc = []
        exp = [
            [-2, 0],
            [2, 0],
            [math.sqrt(3), -1],
            [-math.sqrt(3), -1]
        ]

        acc.append(newton_method(A, b, [-1.9, 0.54]))
        acc.append(newton_method(A, b, [2.5, 0.54]))
        acc.append(newton_method(A, b, [1.8, -1.1]))
        acc.append(newton_method(A, b, [-1.5, -0.54]))

        for a, e in zip(acc, exp):
            self.assertAlmostEqual(a[0], e[0], None, None, DEFAULT_DELTA)
            self.assertAlmostEqual(a[1], e[1], None, None, DEFAULT_DELTA)
