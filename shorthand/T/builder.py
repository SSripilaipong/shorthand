from typing import Any, Callable

from shorthand.T.transformation import Transformation


_getattr = getattr
_EMPTY = type("_EMPTY", (), {})()


def add(x: Any) -> Transformation:
    return Transformation(lambda t: t + x)


def sub_by(x: Any) -> Transformation:
    return Transformation(lambda t: t - x)


def sub_from(x: Any) -> Transformation:
    return Transformation(lambda t: x - t)


def mul(x: Any) -> Transformation:
    return Transformation(lambda t: t * x)


def div_by(x: Any) -> Transformation:
    return Transformation(lambda t: t / x)


def div_from(x: Any) -> Transformation:
    return Transformation(lambda t: x / t)


def floordiv_by(x: Any) -> Transformation:
    return Transformation(lambda t: t // x)


def floordiv_from(x: Any) -> Transformation:
    return Transformation(lambda t: x // t)


def pow(x: Any) -> Transformation:
    return Transformation(lambda t: t ** x)


def getattr(key: Any, default: Any = _EMPTY) -> Transformation:
    if default is _EMPTY:
        return Transformation(lambda t: _getattr(t, key))
    return Transformation(lambda t: _getattr(t, key, default))


def do(f: Callable[[Any], Any]) -> Transformation:
    def _do(x: Any) -> Any:
        f(x)
        return x
    return Transformation(_do)
