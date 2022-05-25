from typing import Any, Callable


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
