from functools import reduce

from shorthand import A, T
from shorthand.transformation.transformation import Transformation


def main(n: int):
    fibonacci = A.current() >> T.do(Transformation(lambda x: x[-1] + x[-2]) >> ...)
    print(reduce(fibonacci, range(n), [0, 1]))


if __name__ == "__main__":
    main(7)
