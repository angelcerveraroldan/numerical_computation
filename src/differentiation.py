_default_diff = 0.000001


def differentiate_real_fn(fn, x, diff=_default_diff):
    """
    Differentiate a function at a given value x

    Note that if you differentiate a function at some input where it is not defined, you will still get some output, but it will be nonsense. Make sure that the function can be differentiated befere trying to do so!

    Eg: d/dx (1/x) at x = 0 is equal to 100000000000000.0 

    @param fn from real to real
    @param x where to evaluate the functions derivative
    @param diff value of h in derivative definition, default value is given

    @returns the derivatives value evaluated at x
    """

    return (fn(x + diff) - fn(x - diff)) / (2 * diff)


def differentiate_real_fn_accurate(fn, x, diff=_default_diff):
    """
    Differentiate a function at a given value x, this function proved more accuracy than differential_real_fn

    Note that if you differentiate a function at some input where it is not defined, you will still get some output, but it will be nonsense. Make sure that the function can be differentiated befere trying to do so!

    Eg: d/dx (1/x) at x = 0 is equal to 100000000000000.0 

    @param fn from real to real
    @param x where to evaluate the functions derivative
    @param diff value of h in derivative definition, default value is given

    @returns the derivatives value evaluated at x
    """

    return (- fn(x + 2 * diff) + 8 * fn(x + diff) - 8 * fn(x - diff) + fn(x - 2 * diff)) / (12 * diff)


def jacobian(functions, x, diff=_default_diff):
    """
    Numerical approximation of the jacobian of an array of functions $f: RR^m -> RR$

    @param functions an array of functions, each of which takes in an array of m real numbers and returns one real number
    @param x where to evaluate the jacobian (an m dim vector) 
    @param diff value of h in derivative definition, default value is given

    @returns jacobian matrix evaluated at the given x
    """

    def _plus_minus(v1, v2):
        plus = list(map(lambda x, y: x + y, v1, v2))
        minus = list(map(lambda x, y: x - y, v1, v2))

        return plus, minus

    input_size = len(x)
    jacobian = []

    for function in functions:
        # The function differentiated at each input and evaluated at x 
        function_differentials = []
        for i in range(input_size):
            diff_vector = [diff if i == j else 0 for j in range(0, input_size)]
            small, large = _plus_minus(x, diff_vector)

            evaluates = (function(small) - function(large)) / (2 * diff)
            function_differentials.append(evaluates)

        jacobian.append(function_differentials)

    return jacobian
