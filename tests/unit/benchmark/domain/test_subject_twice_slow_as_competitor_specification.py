# -*- coding: utf-8 -*-

from tests.fixtures.benchmark import ComparativeBenchmarkMother
from bench.app.benchmark.domain.specification import SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification
from bench.app.benchmark.domain.value_objects import PageBenchmark

specification = SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification()


def test_it_should_return_true_if_subject_url_loaded_twice_as_slow_as_at_least_one_of_competitors():
    # given
    subject_benchmark = PageBenchmark('some url', 4)
    competitor_benchmark = PageBenchmark('another url', 2)
    benchmark = ComparativeBenchmarkMother.create_any_with(subject_benchmark, competitor_benchmark)

    # when
    result = specification.is_satisfied_by(benchmark)

    # then
    assert result is True


def test_it_should_return_false_if_subject_url_loaded_faster_than_competitors():
    # given
    subject_benchmark = PageBenchmark('some url', 2)
    competitor_benchmark = PageBenchmark('another url', 3)
    benchmark = ComparativeBenchmarkMother.create_any_with(subject_benchmark, competitor_benchmark)

    # when
    result = specification.is_satisfied_by(benchmark)

    # then
    assert result is False


def test_it_should_return_false_if_subject_url_loaded_in_same_time_than_competitors():
    # given
    subject_benchmark = PageBenchmark('some url', 3)
    competitor_benchmark = PageBenchmark('another url', 3)
    benchmark = ComparativeBenchmarkMother.create_any_with(subject_benchmark, competitor_benchmark)

    # when
    result = specification.is_satisfied_by(benchmark)

    # then
    assert result is False
