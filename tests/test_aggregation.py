from functools import reduce

from shorthand import A


def test_add():
    assert reduce(A.add(), range(4)) == 6
