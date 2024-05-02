from src.differentiation import *


def main():
    out = differentiate_real_fn(lambda x: 1 / x, 0)
    print(out)


if __name__ == "__main__":
    main()
