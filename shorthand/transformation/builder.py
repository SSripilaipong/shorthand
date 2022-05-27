from collections import defaultdict
from typing import Any, Callable, Dict

from shorthand.transformation.transformation import Transformation


_EMPTY = type("_EMPTY", (), {})()


class TransformationBuilder:
    def __init__(self, key: Any = _EMPTY):
        self._key = key

    def add(self, x: Any) -> Transformation:
        return self._build(lambda t: t + x)

    def sub_by(self, x: Any) -> Transformation:
        return self._build(lambda t: t - x)

    def sub_from(self, x: Any) -> Transformation:
        return self._build(lambda t: x - t)

    def mul(self, x: Any) -> Transformation:
        return self._build(lambda t: t * x)

    def div_by(self, x: Any) -> Transformation:
        return self._build(lambda t: t / x)

    def div_from(self, x: Any) -> Transformation:
        return self._build(lambda t: x / t)

    def floordiv_by(self, x: Any) -> Transformation:
        return self._build(lambda t: t // x)

    def floordiv_from(self, x: Any) -> Transformation:
        return self._build(lambda t: x // t)

    def pow(self, x: Any) -> Transformation:
        return self._build(lambda t: t ** x)

    def attr(self, key: Any, default: Any = _EMPTY) -> Transformation:
        if default is _EMPTY:
            return Transformation(lambda t: getattr(t, key))
        return self._build(lambda t: getattr(t, key, default))

    def do(self, f: Callable, *args, **kwargs) -> Transformation:
        def _do(x: Any) -> Any:
            f(x, *args, **kwargs)
            return x
        return self._build(_do)

    def repeat(self, s: str) -> Transformation:
        return self._build(lambda n: s * n)

    def get(self, key: Any, default: Any = _EMPTY) -> Transformation:
        if default is _EMPTY:
            return Transformation(lambda x: x[key])
        return self._build(lambda x: x.get(key, default))

    def item(self, key: Any) -> Transformation:
        return self._build(lambda x: x[key])

    def select(self, condition: Callable[[Any], bool], true: Callable[[Any], Any], false: Callable[[Any], Any]) \
            -> Transformation:
        return self._build(lambda x: true(x) if condition(x) else false(x))

    def val(self, v: Any) -> Transformation:
        return self._build(lambda x: v)

    def me(self) -> Transformation:
        return self._build(lambda x: x)

    def safe(self, f: Callable[[Any], Any], default: Any) -> Transformation:
        def _f(x: Any) -> Any:
            try:
                return f(x)
            except BaseException:
                return default
        return self._build(_f)

    def error(self, f: Callable[[Any], Any]) -> Transformation:
        def _f(x: Any) -> Any:
            try:
                f(x)
                return None
            except BaseException as e:
                return e
        return self._build(_f)

    def wrap(self, key: Any, default: Any = _EMPTY) -> Transformation:
        if default is _EMPTY:
            return self._build(lambda x: {key: x})
        return self._build(lambda x: defaultdict(lambda: default, [(key, x)]))

    def __getitem__(self, key: Any) -> 'TransformationBuilder':
        return TransformationBuilder(key)

    def _build(self, f: Callable[[Any], Any]) -> Transformation:
        if self._key is _EMPTY:
            return Transformation(f)

        def _f(x: Any) -> Any:
            x[self._key] = f(x[self._key])
            return x

        return Transformation(_f)

    def project(self, template: Dict[Any, Callable[[Any], Any]]) -> Transformation:
        def _f(x: Any) -> Any:
            return {key: t(x) for key, t in template.items()}
        return self._build(_f)


T: TransformationBuilder = TransformationBuilder()
