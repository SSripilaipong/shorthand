from typing import Any, Callable


class Proposition:
    def __init__(self, f: Callable[[Any], bool]):
        self._f = f

    def __call__(self, x: Any) -> bool:
        return self._f(x)

    def __and__(self, other: 'Proposition') -> 'Proposition':
        return Proposition(lambda x: self(x) & other(x))
