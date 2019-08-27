# -*- coding: utf-8 -*-

from bench.app.benchmark.domain.entities import ComparativeBenchmark
from bench.app.core.domain.specification import Specification


class SubjectLoadedSlowerThanAtLeastOneOfCompetitorsSpecification(Specification):

    def is_satisfied_by(self, benchmark: ComparativeBenchmark) -> bool:
        for competitor in benchmark.competitors_benchmarks:
            if benchmark.subject_benchmark.load_time > competitor.load_time:
                return True
        return False


class SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification(Specification):

    def is_satisfied_by(self, benchmark: ComparativeBenchmark) -> bool:
        for competitor in benchmark.competitors_benchmarks:
            if benchmark.subject_benchmark.load_time >= competitor.load_time * 2:
                return True
        return False
