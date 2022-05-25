from typing import Any, Callable, Collection

_FilterBuilderType = Callable[[Any], bool]


def is_(x: Any) -> _FilterBuilderType:
    return lambda t: t is x


def is_not(x: Any) -> _FilterBuilderType:
    return lambda t: t is not x


def eq(x: Any) -> _FilterBuilderType:
    return lambda t: t == x


def neq(x: Any) -> _FilterBuilderType:
    return lambda t: t != x


def lt(x: Any) -> _FilterBuilderType:
    return lambda t: t < x


def le(x: Any) -> _FilterBuilderType:
    return lambda t: t <= x


def gt(x: Any) -> _FilterBuilderType:
    return lambda t: t > x


def ge(x: Any) -> _FilterBuilderType:
    return lambda t: t >= x


def is_in(x: Collection) -> _FilterBuilderType:
    return lambda t: t in x


def is_not_in(x: Collection) -> _FilterBuilderType:
    return lambda t: t not in x


def check(t: Callable[[Any], Any], f: Callable[[Any], bool]) -> _FilterBuilderType:
    return lambda x: f(t(x))
