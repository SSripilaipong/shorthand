from typing import Any, Callable


def is_(x: Any) -> Callable[[Any], bool]:
    return lambda t: t is x


def is_not(x: Any) -> Callable[[Any], bool]:
    return lambda t: t is not x


def eq(x: Any) -> Callable[[Any], bool]:
    return lambda t: t == x


def neq(x: Any) -> Callable[[Any], bool]:
    return lambda t: t != x


def lt(x: Any) -> Callable[[Any], bool]:
    return lambda t: t < x
