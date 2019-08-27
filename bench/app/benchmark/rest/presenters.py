# -*- coding: utf-8 -*-

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.core.rest.presenters import Presenter


class ComparativeBenchmarkPresenter(Presenter):

    @staticmethod
    def from_object(benchmark: ComparativeBenchmark):
        presentation = {
            'id': benchmark.benchmark_id,
            'date': benchmark.date,
            'subject_url': benchmark.subject_benchmark.url,
            'subject_load_time': benchmark.subject_benchmark.load_time,
        }

        competitors = []

        for competitor_benchmark in benchmark.competitors_benchmarks:
            competitors.append({
                'url': competitor_benchmark.url,
                'load_time': competitor_benchmark.load_time
            })

        presentation.update({'competitors': competitors})

        return presentation

