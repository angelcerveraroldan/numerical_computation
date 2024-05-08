import numpy as np
import scipy as sc
import matplotlib.pyplot as plt


def vandermonde(x_data, fx_data):
    """x
    Creates a vandermonde Polynomial to approximate an unknown function with known values
    @param x_data: Inputs to the unknown function with known outputs
    @param fx_data: The output values of each x
    @return: A matrix representation of the vandermonde polynomial
    """
    v = np.vander(x_data)
    return np.linalg.solve(v, fx_data)


def lagrangian(x_data, fx_data):
    """
    Creates a lagrangian Polynomial to approximate an unknown function with known values
    @param x_data: Inputs to the unknown function with known outputs
    @param fx_data: The output values of each x
    @return: A matrix representation of the lagrangian polynomial
    """
    return sc.interpolate.lagrange(x_data, fx_data)


def _poly_newton_coefficient(x, y):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    m = len(x)

    x = np.copy(x)
    a = np.copy(y)
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

    return a


def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = _poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p


x = np.array([25, 50, 75])
fx = np.array([829800, 3298250, 7405450])
print(x)
print(fx)
print()
print(vandermonde(x, fx))
print(lagrangian(x, fx))

print(newton_polynomial(x, fx, 0))
