from src.constants import DEFAULT_DELTA
from src.differentiation import jacobian
import numpy as np
import scipy as sc


def _is_close_to_zero(arr, delta=DEFAULT_DELTA):
    for i in arr:
        if abs(i) > delta:
            return False
    return True


def newton_method(matrix, b, guess):
    # Find the functions
    def f(n, x):
        total = 0
        for i in range(len(matrix[n])):
            total += (matrix[n][i](x) * x[i])
        return total

    functions = list(map(
        lambda r: lambda x: (f(r, x)) - b[r],
        range(len(matrix))
    ))

    # Start the algorithm here
    current_guess = guess

    while True:
        output = [f(current_guess) for f in functions]
        if _is_close_to_zero(output):
            break

        jacobians = jacobian(functions, current_guess)
        delta = np.linalg.solve(jacobians, -1 * np.array(output))
        current_guess = list(map(lambda a, b: a + b, current_guess, delta))

    return current_guess
