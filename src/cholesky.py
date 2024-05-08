import scipy.linalg as ln

def cholesky(A):
    """
    Read cholesky.md file
    @param A: symmetric and positive definite matrix
    @return: upper triangular matrix C such that A=C^T*C
    """
    return ln.cholesky(A)
