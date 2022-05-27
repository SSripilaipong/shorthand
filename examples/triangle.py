from shorthand.transformation import T


def main(n: int):
    print_triangle = T.do(T.sub_from(n) >> T.repeat(" ") >> T.do(print, end="")) >> \
                     T.do(T.repeat("*") >> T.do(print))
    list(map(print_triangle, range(1, n+1)))


if __name__ == "__main__":
    main(7)
