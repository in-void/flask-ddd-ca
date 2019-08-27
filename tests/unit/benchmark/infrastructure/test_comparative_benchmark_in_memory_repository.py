# -*- coding: utf-8 -*-

from tests.fixtures.benchmark import ComparativeBenchmarkMother
from bench.app.benchmark.domain.exceptions import ComparativeBenchmarkNotFound
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository


def test_it_should_find_benchmark_by_id():
    # given
    benchmark_id = '1'
    benchmark = ComparativeBenchmarkMother.create_any_with_id(benchmark_id)

    # when
    benchmark_repository = ComparativeBenchmarkInMemoryRepository()
    benchmark_repository.add(benchmark)

    # then
    found_benchmark = benchmark_repository.get_by_id(benchmark_id)
    assert found_benchmark == benchmark


def test_it_should_inform_when_benchmark_not_found():
    # given
    benchmark_id = '1'
    benchmark_repository = ComparativeBenchmarkInMemoryRepository()

    try:
        # when
        benchmark_repository.get_by_id(benchmark_id)
    except ComparativeBenchmarkNotFound as error:
        # then
        assert error.benchmark_id == benchmark_id
