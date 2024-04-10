import numpy as np

EPSILON = 0.000000001

# The functions that were given to us
functions = [
    # i is an array
    lambda i: 7 * i[0]**3 - 10 * i[0] - i[1] - 1,
    lambda i: 8 * i[1]**3 - 11 * i[1] + i[0] - 1
]


jacobian_fn =  [
    # Derivatives of f1
    [
        lambda i: 21 * i[0]**2 - 10,
        lambda i: - 1,
    ],

    # Derivatives of f2
    [
        lambda i: 1, 
        lambda i: 24 * i[1]**2 - 11 
    ],
]

# Evaluaet the jacobian at some x
def eval_jacobian(x):
    ans = []
    for row in jacobian_fn:
        new_row = []

        for derivative in row: 
            new_row.append(derivative(x))

        ans.append(new_row)
        new_row = []

    return ans

def newtons_method():
    # This is the initial guess, maybe use wolfram to get a decent one
    # since it can impact the solution
    guess = [1, 1]

    while(True):
        # print(f"iter >> {guess}")

        eval = []
        for f in functions: 
            eval.append(f(guess))


        # Check if the guess is good enogh
        if max(map(abs, eval)) < EPSILON: 
           return guess; 


        # Get the jacobian matrix at the current guess
        jacobian = eval_jacobian(guess)   
        delta = np.linalg.solve(jacobian, - np.array(eval))
        guess += delta

print(newtons_method())
