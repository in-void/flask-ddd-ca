# -*- coding: utf-8 -*-

from typing import List

from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.core.domain import Aggregate


class ComparativeBenchmark(Aggregate):

    def __init__(self, benchmark_id: str, date: str, subject_benchmark: PageBenchmark,
                 competitors_benchmarks: List[PageBenchmark]) -> None:

        super().__init__()

        self.benchmark_id = benchmark_id
        self.date = date
        self.subject_benchmark = subject_benchmark
        self.competitors_benchmarks = competitors_benchmarks
