import numpy as np

MinusInf = -np.inf
Inf = np.inf

Frobenius = 'fro'
Nuclear = 'nuc'

MinusTwo = -2
MinusOne = -1
Zero = 0
One = 1
Two = 2


def get_norm(matrix, norm):
    return np.linalg.norm(matrix, ord=norm)
