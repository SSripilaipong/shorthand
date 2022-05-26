from typing import Any, Callable, Collection

from shorthand.P.proposition import Proposition


def is_(x: Any) -> Proposition:
    return Proposition(lambda t: t is x)


def is_not(x: Any) -> Proposition:
    return Proposition(lambda t: t is not x)


def eq(x: Any) -> Proposition:
    return Proposition(lambda t: t == x)


def neq(x: Any) -> Proposition:
    return Proposition(lambda t: t != x)


def lt(x: Any) -> Proposition:
    return Proposition(lambda t: t < x)


def le(x: Any) -> Proposition:
    return Proposition(lambda t: t <= x)


def gt(x: Any) -> Proposition:
    return Proposition(lambda t: t > x)


def ge(x: Any) -> Proposition:
    return Proposition(lambda t: t >= x)


def is_in(x: Collection) -> Proposition:
    return Proposition(lambda t: t in x)


def is_not_in(x: Collection) -> Proposition:
    return Proposition(lambda t: t not in x)


def check(t: Callable[[Any], Any], f: Callable[[Any], bool]) -> Proposition:
    return Proposition(lambda x: f(t(x)))


def between(start: Any, end: Any, *, left: bool = True, right: bool = True) -> Proposition:
    if left and right:
        return Proposition(lambda x: start <= x <= end)
    if not left:
        if not right:
            return Proposition(lambda x: start < x < end)
        return Proposition(lambda x: start < x <= end)
    return Proposition(lambda x: start <= x < end)
