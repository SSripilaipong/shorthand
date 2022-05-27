from typing import Any, Callable


class Aggregation:
    def __init__(self, f: Callable[[Any, Any], Any]):
        self._f = f

    def __call__(self, current: Any, new: Any):
        return self._f(current, new)
