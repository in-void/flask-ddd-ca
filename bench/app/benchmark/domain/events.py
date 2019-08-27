# -*- coding: utf-8 -*-

from bench.app.core.domain.events_dispatcher import DomainEvent


class ComparativeBenchmarkFinished(DomainEvent):

    name: str = 'benchmark.comparative_benchmark_finished'

    def __init__(self, benchmark_id: str) -> None:
        super().__init__()

        self.benchmark_id = benchmark_id
