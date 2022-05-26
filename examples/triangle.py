from shorthand.T import *


def main(n: int):
    print_triangle = do(sub_from(n) >> repeat(" ") >> do(print, end="")) >> \
                     do(repeat("*") >> do(print))
    list(map(print_triangle, range(1, n+1)))


if __name__ == "__main__":
    main(7)
