from shorthand.aggregation.aggregation import Aggregation


class AggregationBuilder:
    def add(self) -> Aggregation:
        return self._build()

    def _build(self) -> Aggregation:
        return Aggregation(lambda current, new: current + new)


A: AggregationBuilder = AggregationBuilder()
