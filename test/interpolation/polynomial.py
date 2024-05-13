import unittest

import numpy as np

from src.constants import DEFAULT_DELTA
from src.interpolation.polynomial import vandermonde_manual


class InterpolationVandermondeTest(unittest.TestCase):
    def test_notes(self):
        self.assertTrue(np.allclose(
            vandermonde_manual([(-2, -2), (-1, 1), (2, -1)]),
            [2.1667, 0.25, -0.9167],
            atol=0.0001
        ))
