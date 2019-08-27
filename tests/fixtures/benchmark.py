# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.benchmark.domain.value_objects import PageBenchmark
from bench.app.benchmark.use_cases.commands import CreateComparativeWebPagesBenchmarkCommand


class ComparativeBenchmarkMother(object):

    @staticmethod
    def create_comparative_benchmark_with_fixed_load_time(benchmark_id: str,
                                                          subject_url: str,
                                                          competitors_urls: List[str],
                                                          load_time) -> ComparativeBenchmark:

        subject_benchmark = PageBenchmark(subject_url, load_time)

        competitors_benchmarks = [PageBenchmark(u, load_time) for u in competitors_urls]

        datetime_str = str(datetime.now())

        return ComparativeBenchmark(benchmark_id, datetime_str, subject_benchmark, competitors_benchmarks)

    @staticmethod
    def create_any_with_id(benchmark_id: str) -> ComparativeBenchmark:
        subject_benchmark = PageBenchmark('some url', 1)

        competitors_benchmarks = [PageBenchmark('another url', 1)]

        datetime_str = str(datetime.now())

        return ComparativeBenchmark(benchmark_id, datetime_str, subject_benchmark, competitors_benchmarks)

    @staticmethod
    def create_any_with_competitor(competitor_benchmark: PageBenchmark) -> ComparativeBenchmark:
        subject_benchmark = PageBenchmark('some url', 1)

        competitors_benchmarks = [competitor_benchmark]

        datetime_str = str(datetime.now())

        return ComparativeBenchmark('1', datetime_str, subject_benchmark, competitors_benchmarks)

    @staticmethod
    def create_any_with(subject_benchmark: PageBenchmark, competitor_benchmark: PageBenchmark) -> ComparativeBenchmark:
        competitors_benchmarks = [competitor_benchmark]

        datetime_str = str(datetime.now())

        return ComparativeBenchmark('1', datetime_str, subject_benchmark, competitors_benchmarks)

    @staticmethod
    def create_any() -> ComparativeBenchmark:
        subject_benchmark = PageBenchmark('some url', 1)
        competitors_benchmarks = [PageBenchmark('another url', 1)]

        datetime_str = str(datetime.now())

        return ComparativeBenchmark('1', datetime_str, subject_benchmark, competitors_benchmarks)


class CreateComparativeWebPagesBenchmarkCommandMother(object):

    @staticmethod
    def create_any() -> CreateComparativeWebPagesBenchmarkCommand:
        command = CreateComparativeWebPagesBenchmarkCommand()

        command.benchmark_id = '1'
        command.subject_url = 'some-url'
        command.competitors_urls = ['another url']

        return command
