from shorthand import T


def test_add():
    assert list(map(T.add(1), [1, 2, 3])) == [2, 3, 4]


def test_subtract_by():
    assert list(map(T.subtract_by(1), [1, 2, 3])) == [0, 1, 2]


def test_subtract_from():
    assert list(map(T.subtract_from(1), [1, 2, 3])) == [0, -1, -2]
