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


def test_pow():
    assert list(map(T.pow(3), [1, 2, 3])) == [1., 8., 27.]


def test_getattr():
    class C:
        def __init__(self, v):
            self.v = v

    assert list(map(T.getattr("v"), [C(1), C(4)])) == [1, 4]


def test_getattr_with_default():
    class C:
        def __init__(self, v):
            self.v = v

    class D:
        pass

    assert list(map(T.getattr("v", -1), [C(1), D(), C(4)])) == [1, -1, 4]


def test_do():
    d = []
    assert list(map(T.do(d.append), range(5))) == [0, 1, 2, 3, 4]
    assert d == [0, 1, 2, 3, 4]


def test_do_with_params():
    class M:
        def __call__(self, x, p, q):
            self.params = x, p, q

    m = M()
    list(map(T.do(m, 1, q=True), ["x"]))
    assert m.params == ("x", 1, True)


def test_pipe():
    d = []
    assert list(map(T.do(d.append) > T.mul(2), range(5))) == [0, 2, 4, 6, 8]
    assert d == [0, 1, 2, 3, 4]


def test_repeat_str():
    assert list(map(T.repeat("*"), range(3))) == ["", "*", "**"]
