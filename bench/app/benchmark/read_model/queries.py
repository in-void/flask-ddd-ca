# -*- coding: utf-8 -*-


class BenchmarkQuery(object):

    benchmark_id: str

    @classmethod
    def find_by_id(cls, benchmark_id: str):
        query = cls()

        query.benchmark_id = benchmark_id

        return query
