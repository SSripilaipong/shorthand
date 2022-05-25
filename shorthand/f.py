from typing import Any, Callable


def is_(t: Any) -> Callable[[Any], bool]:
    return lambda x: x is t


def is_not(t: Any) -> Callable[[Any], bool]:
    return lambda x: x is not t
