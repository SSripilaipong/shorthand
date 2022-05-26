from shorthand import T


def test_add():
    assert list(map(T.add(1), [1, 2, 3])) == [2, 3, 4]


def test_sub_by():
    assert list(map(T.sub_by(1), [1, 2, 3])) == [0, 1, 2]


def test_sub_from():
    assert list(map(T.sub_from(1), [1, 2, 3])) == [0, -1, -2]


def test_mul():
    assert list(map(T.mul(2), [1, 2, 3])) == [2, 4, 6]


def test_div_by():
    assert list(map(T.div_by(2), [1, 2, 3])) == [.5, 1., 1.5]


def test_div_from():
    assert list(map(T.div_from(6), [1, 2, 3])) == [6., 3., 2.]


def test_floordiv_by():
    assert list(map(T.floordiv_by(2), [1, 2, 3])) == [0., 1., 1.]


def test_floordiv_from():
    assert list(map(T.floordiv_from(7), [1, 2, 3])) == [7., 3., 2.]
