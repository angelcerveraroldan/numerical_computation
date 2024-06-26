import numpy as np
from numpy import linalg as LA

def add_rows(matrix, i, j):
    """
    Add row i of a matrix with row j

    @param matrix
    @param i the first index
    @param j the second index

    @return the array matrix[i] + matrix[j]
    """
    f = matrix[i]
    s = matrix[j]

    arr = []
    for i in range(0, len(f)):
        arr.append(f[i] + s[i])

    return arr


def sub_rows(matrix, i, j):
    """
    Subtract row i of a matrix with row j

    @param matrix
    @param i the first index
    @param j the second index

    @return the array matrix[i] - matrix[j]
    """
    f = matrix[i]
    s = matrix[j]

    arr = []
    for i in range(0, len(f)):
        arr.append(f[i] - s[i])

    return arr


def add_rows_scalar(matrix, i, j, c):
    """
    adds replaces matrix[i] with matrix[i]+(c*matrix[j])
    @param matrix:
    @param i: row being added to
    @param j: row being added
    @param c: scalar
    @return: new matrix
    """
    ret = np.asfarray(matrix.copy())
    ret[i] = ret[i]+(c*ret[j])
    return ret


def row_swap(matrix, i, j):
    """
    Swap two rows in a matrix

    @param matrix
    @param i index
    @param j index

    @return nothing, matrix is mutated
    """

    tmp = matrix[i].copy()
    matrix[i] = matrix[j]
    matrix[j] = tmp


def scalar_row(matrix, i, scalar):
    """
    Multiply every element in a row by some factor

    @param matrix
    @param i index
    @param scalar number
    
    @return nothing, matrix is mutated
    """

    matrix[i] = list(map(lambda x: x * scalar, matrix[i]))


def pivot(matrix, i):
    """
    Pivot around a column, this will make it so that the value at matrix[i][i]
    is the largest value of matrix[i][i], matrix[i+1][i], ...
    
    @param matrix
    @param i index of the column to pivot

    @return nothing, matrix is mutated
    """

    at, max = i, matrix[i][i]
    for j in range(i, len(matrix)):
        val = matrix[j][i]
        if val > max:
            max = val
            at = j

    row_swap(matrix, i, at)


def eigenthangs(matrix):
    npmatrix = np.array(matrix)
    eigenvalues, eigenvectors = LA.eig(npmatrix)
    return eigenvalues, eigenvectors