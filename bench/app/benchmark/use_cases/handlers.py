# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.infrastructure.page_benchmark import PageBenchmarker
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkRepository
from bench.app.benchmark.use_cases.commands import CreateComparativeWebPagesBenchmarkCommand
from bench.app.core.domain.events_dispatcher import DomainEventsDispatcherMixin


class CreateComparativeWebPagesBenchmarkHandler(DomainEventsDispatcherMixin):

    def __init__(self, benchmark_repository: ComparativeBenchmarkRepository, benchmark: PageBenchmarker) -> None:
        super().__init__()

        self.benchmark_repository = benchmark_repository
        self.benchmark = benchmark

    def handle(self, command: CreateComparativeWebPagesBenchmarkCommand) -> None:
        subject_benchmark = self.benchmark_url(command.subject_url)
        competitors_benchmarks = self.benchmark_competitors_urls(command.competitors_urls)

        self.store_results(command.benchmark_id, subject_benchmark, competitors_benchmarks)

        self.fire_event(ComparativeBenchmarkFinished(command.benchmark_id))

    def store_results(self, benchmark_id: str, subject_benchmark: PageBenchmark, competitors_benchmarks: List[PageBenchmark]) -> None:
        current_datetime = str(datetime.now())

        comparative_benchmark = ComparativeBenchmark(benchmark_id, current_datetime, subject_benchmark, competitors_benchmarks)

        self.benchmark_repository.add(comparative_benchmark)

    def benchmark_competitors_urls(self, competitors_urls: List[str]) -> List[PageBenchmark]:
        competitors_benchmarks = []

        for competitor_url in competitors_urls:
            competitors_benchmarks.append(self.benchmark_url(competitor_url))

        return competitors_benchmarks

    def benchmark_url(self, url: str) -> PageBenchmark:
        return self.benchmark.measure_page_load(url)
