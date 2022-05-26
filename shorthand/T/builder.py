from typing import Any

from shorthand.T.transformation import Transformation


def add(x: Any) -> Transformation:
    return Transformation(lambda t: t + x)
