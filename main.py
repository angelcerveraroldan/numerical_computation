import numpy as np

from linear_systems.gaussian import reduced_form


def main(): 
    reduced_form(np.array([
        [3.0, 6, 9, 39],
        [2.0, 5, -2, 3],
        [1.0, 3, -1, 2]
    ]))

if __name__ == "__main__": 
    main()
