from functools import reduce

from shorthand import A


def test_add():
    assert reduce(A.add(), range(4)) == 6


def test_mul():
    assert reduce(A.mul(), range(1, 6)) == 120
