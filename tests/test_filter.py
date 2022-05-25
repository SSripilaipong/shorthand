from shorthand import F


def test_is_x():
    assert list(filter(F.is_(123), [0, 123, 4, 567, 123])) == [123, 123]


def test_is_not_x():
    assert list(filter(F.is_not(123), [0, 123, 4, 567, 123])) == [0, 4, 567]


def test_eq():
    assert list(filter(F.eq(123), [0, 123, 4, 567, 123])) == [123, 123]


def test_neq():
    assert list(filter(F.neq(123), [0, 123, 4, 567, 123])) == [0, 4, 567]


def test_lt():
    assert list(filter(F.lt(50), [0, 123, 4, 567, 123])) == [0, 4]


def test_le():
    assert list(filter(F.le(4), [0, 123, 4, 567, 123])) == [0, 4]


def test_gt():
    assert list(filter(F.gt(4), [0, 123, 4, 567, 123])) == [123, 567, 123]


def test_ge():
    assert list(filter(F.ge(123), [0, 123, 4, 567, 123])) == [123, 567, 123]


def test_is_in():
    assert list(filter(F.is_in(["abc", 0, 567]), [0, 123, 4, 567, 123, "abc"])) == [0, 567, "abc"]
