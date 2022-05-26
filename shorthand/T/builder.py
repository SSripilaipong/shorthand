from typing import Any

from shorthand.T.transformation import Transformation


def add(x: Any) -> Transformation:
    return Transformation(lambda t: t + x)


def sub_by(x: Any) -> Transformation:
    return Transformation(lambda t: t - x)


def sub_from(x: Any) -> Transformation:
    return Transformation(lambda t: x - t)
