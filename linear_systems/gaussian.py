import numpy as np

from linear_systems.matrix import scalar_row, sub_rows, pivot

def reduced_form(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for rowid in range(0, rows):
        pivot(matrix, rowid)

        if matrix[rowid][rowid] == 0:
            continue

        scalar_row(matrix, rowid, 1/(matrix[rowid][rowid]));

        for r in range(rowid+1, rows):
            if matrix[r][rowid] == 0: 
                continue

            scalar = matrix[rowid][rowid]/matrix[r][rowid]
            print(scalar)

            scalar_row(matrix, r, scalar)
            matrix[r] = sub_rows(matrix, r, rowid)

    print(matrix)

