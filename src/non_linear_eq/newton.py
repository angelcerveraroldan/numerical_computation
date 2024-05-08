import numpy as np
from src.differentiation import jacobian
import scipy.linalg as ln


def newton_non_linear(A, b, epsilon=0.000001, guess=None, print_work=False):
    """
    Solves non linear systems of equations Ax=b using Newton's Method
    @param A: System of n nonlinear equations e.g. lambda x: (x[0] ** 2) - (1.6 * x[0]) - x[1]
    @param b: vector in RR^n
    @param epsilon: margin of error
    @param guess: RR^n vector of initial guesses, default is [1,1,...,1]
    @return: vector in RR^n
    """
    n = len(A)
    assert n == len(b), "A has to be the same length as b"
    if guess is None:
        guess = np.ones(1, n)

    f_arr = list(map(lambda a, c: lambda x: a(x) - c, A, b))

    def f(x):
        """
        Creating a function f(x)=Ax-b
        @param x: vector in RR^n
        @return: vector in RR^n
        """
        return np.array([A[i](x)-b[i] for i in range(n)])

    f_x = f(guess)
    while ln.norm(f_x) > epsilon:
        if print_work:
            print(f"solution: {guess} error: {ln.norm(f_x)}")
        J_x = jacobian(f_arr, guess)
        delta_x = ln.solve(J_x, -1*f_x)
        guess += delta_x
        f_x = f(guess)

    return guess
