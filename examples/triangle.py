from shorthand.T import *


def main(n: int):
    list(map(
        do(do(print, "A") > do(print, "B") > do(print, "C")),
        range(1, n+1)))


if __name__ == "__main__":
    main(7)
