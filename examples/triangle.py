from shorthand.T import *


def main(n: int):
    list(map(
        do(sub_from(n) >> repeat(" ") >> do(print, end="")) >>
        do(repeat("*") >> do(print)),
        range(1, n+1)))


if __name__ == "__main__":
    main(7)
