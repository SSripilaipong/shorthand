from shorthand import P


def test_is_x():
    assert list(filter(P.is_(123), [0, 123, 4, 567, 123])) == [123, 123]


def test_is_not_x():
    assert list(filter(P.is_not(123), [0, 123, 4, 567, 123])) == [0, 4, 567]


def test_eq():
    assert list(filter(P.eq(123), [0, 123, 4, 567, 123])) == [123, 123]


def test_neq():
    assert list(filter(P.neq(123), [0, 123, 4, 567, 123])) == [0, 4, 567]


def test_lt():
    assert list(filter(P.lt(50), [0, 123, 4, 567, 123])) == [0, 4]


def test_le():
    assert list(filter(P.le(4), [0, 123, 4, 567, 123])) == [0, 4]


def test_gt():
    assert list(filter(P.gt(4), [0, 123, 4, 567, 123])) == [123, 567, 123]


def test_ge():
    assert list(filter(P.ge(123), [0, 123, 4, 567, 123])) == [123, 567, 123]


def test_is_in():
    assert list(filter(P.is_in(["abc", 0, 567]), [0, 123, 4, 567, 123, "abc"])) == [0, 567, "abc"]


def test_is_not_in():
    assert list(filter(P.is_not_in(["abc", 0, 567]), [0, 123, 4, 567, 123, "abc"])) == [123, 4, 123]


def test_check():
    result = list(filter(P.check(lambda x: x * 10, lambda x: 0 < x < 5000), [0, 123, 4, 567, 123]))
    assert result == [123, 4, 123]
