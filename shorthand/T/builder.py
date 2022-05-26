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


def do(f: Callable, *args, **kwargs) -> Transformation:
    def _do(x: Any) -> Any:
        f(x, *args, **kwargs)
        return x
    return Transformation(_do)


def repeat(s: str) -> Transformation:
    return Transformation(lambda n: s * n)


def get(key: Any, default: Any = _EMPTY) -> Transformation:
    if default is _EMPTY:
        return Transformation(lambda x: x[key])
    return Transformation(lambda x: x.get(key, default))


def getitem(key: Any) -> Transformation:
    return Transformation(lambda x: x[key])


def switch(condition: Callable[[Any], bool], true: Callable[[Any], Any], false: Callable[[Any], Any]) -> Transformation:
    return Transformation(lambda x: true(x) if condition(x) else false(x))


def val(v: Any) -> Transformation:
    return Transformation(lambda x: v)


def me() -> Transformation:
    return Transformation(lambda x: x)
