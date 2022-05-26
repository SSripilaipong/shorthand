from typing import Any

from shorthand.T.transformation import Transformation


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
