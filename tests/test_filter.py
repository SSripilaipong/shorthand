from shorthand import F


def test_is_x():
    assert list(filter(F.is_(123), [0, 123, 4, 567, 123])) == [123, 123]


def test_is_not_x():
    assert list(filter(F.is_not(123), [0, 123, 4, 567, 123])) == [0, 4, 567]
