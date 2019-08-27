# -*- coding: utf-8 -*-

from unittest.mock import patch

from tests.fixtures.benchmark import ComparativeBenchmarkMother
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository
from bench.app.benchmark.use_cases.listeners.logger_listener import ComparativeBenchmarkFinishedLoggerListener


@patch('bench.app.core.infrastructure.logger.Logger')
def test_it_should_log_benchmark(logger_mock):
    # given
    competitor_benchmark = PageBenchmark('another url', 1)
    benchmark = ComparativeBenchmarkMother.create_any_with_competitor(competitor_benchmark)

    # and
    repository = ComparativeBenchmarkInMemoryRepository()
    repository.add(benchmark)

    # when
    listener = ComparativeBenchmarkFinishedLoggerListener(repository, logger_mock)
    listener.execute(ComparativeBenchmarkFinished(benchmark.benchmark_id))

    # then
    expected_log = "\n".join([
        "id: %s date: %s" % (benchmark.benchmark_id, benchmark.date),
        "subject: %s load time: %s" % (benchmark.subject_benchmark.url, benchmark.subject_benchmark.load_time),
        "competitor: %s load time: %s difference: %s" % (competitor_benchmark.url, competitor_benchmark.load_time,
                                                         competitor_benchmark.load_time - benchmark.subject_benchmark.load_time),
    ])

    logger_mock.info.assert_called_once_with(expected_log)
