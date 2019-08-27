# -*- coding: utf-8 -*-

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkRepository
from bench.app.core.domain.events_dispatcher import DomainEventsListener
from bench.app.core.infrastructure.logger import Logger


class ComparativeBenchmarkFinishedLoggerListener(DomainEventsListener):

    def __init__(self, benchmark_repository: ComparativeBenchmarkRepository, logger: Logger) -> None:
        super().__init__()

        self.logger = logger
        self.benchmark_repository = benchmark_repository

    def execute(self, event: ComparativeBenchmarkFinished):
        benchmark = self.benchmark_repository.get_by_id(event.benchmark_id)

        return self.log_benchmark(benchmark)

    def log_benchmark(self, benchmark: ComparativeBenchmark):
        log_parts = [
            "id: %s date: %s" % (benchmark.benchmark_id, benchmark.date),
            "subject: %s load time: %s" % (benchmark.subject_benchmark.url, benchmark.subject_benchmark.load_time)]

        for competitor in benchmark.competitors_benchmarks:
            competitor_string = self.create_competitor_string_part(benchmark.subject_benchmark, competitor)
            log_parts.append(competitor_string)

        self.logger.info("\n".join(log_parts))

    def create_competitor_string_part(self, subject_benchmark: PageBenchmark, competitor_benchmark: PageBenchmark) -> str:
        competitor_string = "competitor: %s load time: %s " % (competitor_benchmark.url, competitor_benchmark.load_time)

        difference = competitor_benchmark.load_time - subject_benchmark.load_time
        competitor_string += "difference: %s" % (difference)

        return competitor_string
