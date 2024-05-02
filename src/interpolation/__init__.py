import numpy as np
import scipy as sc


# given n points each with x,y values
# Input x values in 'a' and y values in 'b'
def vandermonde(a, b):
    n = len(a)
    v = np.vander(a, n)
    return np.linalg.solve(v, b)


def lagrangian(a, b):
    return sc.interpolate.lagrangian(a, b)


def newton(a, b):
    return sc.interpolate.newton(a, b)

