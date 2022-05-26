from shorthand import T


def test_add():
    assert list(map(T.add(1), [1, 2, 3])) == [2, 3, 4]


def test_sub_by():
    assert list(map(T.sub_by(1), [1, 2, 3])) == [0, 1, 2]


def test_sub_from():
    assert list(map(T.sub_from(1), [1, 2, 3])) == [0, -1, -2]


def test_mul():
    assert list(map(T.mul(2), [1, 2, 3])) == [2, 4, 6]
