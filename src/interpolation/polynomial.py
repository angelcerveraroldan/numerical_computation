import numpy as np


def vandermonde_manual(pairs, show=False):
    """
    Given k points (xk, f(xk)), find a polynomial of order k-1
    that approximates the function f.

    @param pairs: Array of tuples in the form (x_n, f(x_n))
    @return: Polynomials coefficients
    """

    height = len(pairs)
    matrix = []
    output = []

    for xn, fxn in pairs:
        row = [xn ** i for i in range(height)]
        matrix.append(row)
        output.append(fxn)

    coefficients = np.linalg.solve(
        np.array(matrix),
        np.array(output))

    if show:
        power = 0
        strv = ""
        for coefficient in coefficients:
            prettyx = ("x^" + str(power)) if power > 0 else ""
            strv += (str(coefficient) + prettyx + " + ")
            power += 1

        print(strv[:-3])

    return coefficients


def newton_polynomial(pairs):
    inputs = np.array(list(map(lambda x: x[0], pairs)))
    outputs = np.array(list(map(lambda x: x[1], pairs)))
    ln = len(inputs)
    for i in range(1, ln):
        top = outputs[i:ln] - outputs[i - 1]
        btm = inputs[i:ln] - inputs[i - 1]
        outputs[i:ln] = top / btm

    return outputs

def lagrangian_basis(pairs, x):
    """
    Given k points (xk, f(xk)), estimate the value of f(x)
    using Lagrangian basis.

    @param x: Desired point of estimation
    @param pairs: Array of tuples in the form (x_n, f(x_n))
    @return: Polynomial evaluated at x
    """
    n = len(pairs)
    val = 0

    def l_k(kv):
        prod = 1
        for j in range(n):
            if j == kv:
                continue

            prod *= (x - pairs[j][0]) / (pairs[kv][0] - pairs[j][0])
        return prod

    for k in range(n):
        val += pairs[k][1] * l_k(k)

    return val
