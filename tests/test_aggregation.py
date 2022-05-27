from functools import reduce

from shorthand import A


def test_add():
    assert reduce(A.add(), range(4)) == 6


def test_mul():
    assert reduce(A.mul(), range(1, 6)) == 120


def test_attribute_level_aggregation():
    assert reduce(A["x"].add(), range(4), {"x": 3}) == {"x": 9}


def test_new():
    assert reduce(A.new(), range(10)) == 9
