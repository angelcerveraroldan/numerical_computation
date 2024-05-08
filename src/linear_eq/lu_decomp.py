import numpy as np
import scipy as sc
from src.matrix import add_rows_scalar


def solve_upper_triangular(matrix, ans):
    """
    matrix * x = ans

    @param matrix: An upper triangular matrix. Note that this function will not verify that the matrix really is
    upper triangular. If it isn't, this function will not work.
    @param ans: Desired answer (see formula above)

    @return: Valid value for x vector
    """

    return sc.linalg.solve_triangular(matrix, ans, lower=False, check_finite=False)


def solve_lower_triangular(matrix, ans):
    """
    matrix * x = ans

    @param matrix: A lower triangular matrix. Note that this function will not verify that the matrix really is
    lower triangular. If it isn't, this function will not work.
    @param ans: Desired answer (see formula above)

    @return: Valid value for x vector
    """

    return sc.linalg.solve_triangular(matrix, ans, lower=True, check_finite=False)


def solve(matrix, b):
    """
    Solve Matrix x = b

    @param matrix: Matrix
    @param b: Vector - answer

    @return: vector answer such that matrix times x = b
    """

    return sc.linalg.lu_solve(sc.linalg.lu_factor(matrix), b)


def lu_decomp(matrix):
    """
    This method will use numpy -- P * L * U = matrix

    @param matrix: The matrix to be decomposed

    @return: Permutation, Lower, Upper
    """

    p, l, u = sc.linalg.lu(matrix, permute_l=False)
    return p, l, u

def lu_decomp_no_pp(matrix):
    """
    L * U = matrix
    @param matrix: square matrix
    @return: returns two matrices L U
    """
    n = len(matrix)
    lower = np.zeros((n, n), dtype=np.float64)
    for k in range(n - 1):
        lower[k][k] = 1
        entry_value = matrix[k][k]
        for i in range(k + 1, n):
            c = matrix[i][k] / entry_value
            matrix = add_rows_scalar(matrix, i, k, -c)
            lower[i][k] = c
    lower[n - 1][n - 1] = 1

    return lower, matrix
