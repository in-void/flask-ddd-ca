# -*- coding: utf-8 -*-

from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.infrastructure.page_benchmark import PageBenchmarker


class PageBenchmarkerStub(PageBenchmarker):

    fixed_load_time = 2

    def measure_page_load(self, url: str) -> PageBenchmark:
        return PageBenchmark(url, self.fixed_load_time)
