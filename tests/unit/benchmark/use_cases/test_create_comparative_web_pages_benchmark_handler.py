# -*- coding: utf-8 -*-

from tests.doubles.benchmark import PageBenchmarkerStub
from tests.fixtures.benchmark import CreateComparativeWebPagesBenchmarkCommandMother
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository
from bench.app.benchmark.use_cases.handlers import CreateComparativeWebPagesBenchmarkHandler


def test_it_should_create_benchmarks_for_given_urls():
    # given
    command = CreateComparativeWebPagesBenchmarkCommandMother.create_any()

    # and
    benchmark_repository = ComparativeBenchmarkInMemoryRepository()
    page_benchmarker_stub = PageBenchmarkerStub()

    # when
    comparative_benchmark_handler = CreateComparativeWebPagesBenchmarkHandler(benchmark_repository, page_benchmarker_stub)
    comparative_benchmark_handler.handle(command)

    # then
    stored_benchmark = benchmark_repository.get_by_id(command.benchmark_id)

    assert stored_benchmark.benchmark_id == command.benchmark_id
    assert stored_benchmark.subject_benchmark == PageBenchmark(command.subject_url, 2)

    expected_event = ComparativeBenchmarkFinished(command.benchmark_id)
    assert comparative_benchmark_handler.release_events()[0] == expected_event