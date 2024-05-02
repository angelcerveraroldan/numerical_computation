import unittest, math
import numpy as np

from utils import DEFAULT_DELTA 
from utils.differentiation import differentiate_real_fn, jacobian

class DifferentiationTest(unittest.TestCase):
    def test_differentiate_linear(self):
        # Simple linear function
        fn     = lambda x: 1 + 2 * x
        actual = [differentiate_real_fn(fn, x) for x in range(0, 100)]

        for dif in actual:
            self.assertAlmostEqual(dif, 2, None, None, DEFAULT_DELTA)


    def test_jacobian(self):
        functions = [ 
            lambda inarr: math.cos(inarr[1]) + inarr[0]**3, 
            lambda inarr: inarr[0]**2 + inarr[1] 
        ]

        inputs_outputs = [
                ([0.0, 0.0],   [ [0.0,         0.0], [0.0,  1.0] ]),
                ([1.0, 1.0],   [ [3.0,   -0.841470], [2.0,  1.0] ]),
                ([11.0, 14.0], [ [363.0, -0.990607], [22.0, 1.0] ])
        ]

        for input, output in inputs_outputs:
            jacobian_eval_flattened = np.array(jacobian(functions, input)).flatten()
            expected_flattened = np.array(output).flatten()
   
            for actual, expeceted in zip(jacobian_eval_flattened, expected_flattened):
               self.assertAlmostEqual(actual, expeceted, None, None, DEFAULT_DELTA) 


