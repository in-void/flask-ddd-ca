# -*- coding: utf-8 -*-

from typing import List

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.benchmark.domain.exceptions import ComparativeBenchmarkNotFound


class ComparativeBenchmarkRepository(object):

    def add(self, benchmark: ComparativeBenchmark) -> None:
        raise NotImplementedError()

    def get_by_id(self, benchmark_id: str) -> ComparativeBenchmark:
        raise NotImplementedError()


class ComparativeBenchmarkInMemoryRepository(ComparativeBenchmarkRepository):

    def __init__(self,) -> None:
        super().__init__()

        self._entries: List[ComparativeBenchmark] = []

    def add(self, benchmark: ComparativeBenchmark) -> None:
        self._entries.append(benchmark)

    def get_by_id(self, benchmark_id: str) -> ComparativeBenchmark:

        for benchmark in self._entries:
            if benchmark.benchmark_id == benchmark_id:
                return benchmark

        raise ComparativeBenchmarkNotFound(benchmark_id)
