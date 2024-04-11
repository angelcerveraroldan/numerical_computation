import numpy as np

def add_rows(matrix, i, j):
    f = matrix[i]
    s = matrix[j]

    arr = []
    for i in range(0, len(f)):
        arr.append(f[i]+s[i])

    return np.array(arr)

def sub_rows(matrix, i, j):
    f = matrix[i]
    s = matrix[j]

    arr = []
    for i in range(0, len(f)):
        arr.append(f[i]-s[i])

    return np.array(arr)



def row_swap(matrix, i, j):
    """
    input:
        - matrix : [ [num] ]
        - i      : num
        - j      : num
    """

    tmp = matrix[i].copy()
    matrix[i] = matrix[j]
    matrix[j] = tmp


def scalar_row(matrix, i, scalar):
    """
    input:
        - matrix : [ [num] ]
        - i      : num
          index of the row
        - scalar      : num
          value of scalar multiple
    """

    matrix[i] *= scalar

def pivot(matrix, i):
    """
    input:
        - matrix : [ [num] ]
        - i      : num
          index of the column we want to pivot
    """

    at, max = i, matrix[i][i]
    for j in range(i, len(matrix)):
        val = matrix[j][i]
        if val > max: 
            max = val
            at = j
    
    row_swap(matrix, i, at)


