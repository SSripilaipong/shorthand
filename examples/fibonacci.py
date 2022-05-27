from functools import reduce

from shorthand import A, T


def main(n: int):
    initial = [0, 1]
    fibonacci = A.current() >> T.project([T.item(1), sum])

    print(reduce(fibonacci, range(n), initial)[0])


if __name__ == "__main__":
    main(10)
