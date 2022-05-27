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


def test_current():
    assert reduce(A.current(), range(3, 7)) == 3


def test_attribute_separated_operations():
    assert reduce(A["a"].add() | A["b"].mul(), range(1, 6), {"a": 0, "b": 1}) == {"a": 15, "b": 120}


def test_pipe_in():
    assert reduce(A.add() << (lambda new: new*2), range(6)) == 30


def test_pipe_out():
    assert reduce(A.add() >> (lambda new: new*2), range(6)) == 114


def test_append():
    assert reduce(A.append(), range(6), []) == [0, 1, 2, 3, 4, 5]
