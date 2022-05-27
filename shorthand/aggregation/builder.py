from typing import Callable, Any

from shorthand.aggregation.aggregation import Aggregation


class AggregationBuilder:
    def add(self) -> Aggregation:
        return self._build(lambda current, new: current + new)

    def mul(self) -> Aggregation:
        return self._build(lambda current, new: current * new)

    def _build(self, f: Callable[[Any, Any], Any]) -> Aggregation:
        return Aggregation(f)


A: AggregationBuilder = AggregationBuilder()
