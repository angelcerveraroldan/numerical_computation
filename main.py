import numpy as np
import scipy as sc
from src.interpolation.polynomial import vandermonde_manual, newton_polynomial

def main():
    inp = [
        (10.0, 11381553.0),
        (15.0, 184091718.0),
        (20.0, 1351087483.0),
        (25.0, 6368625348.0),
        (30.0, 22650381813.0),
        (40.0, 168149106543.0),
        (45.0, 382355402808.0),
        (50.0, 797519823673.0),
    ]

    sol = vandermonde_manual(inp[0:3], True)
    sol = newton_polynomial(inp)
    print(sol)


if __name__ == "__main__":
    main()

