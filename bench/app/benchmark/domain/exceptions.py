# -*- coding: utf-8 -*-


class ComparativeBenchmarkNotFound(Exception):

    def __init__(self, benchmark_id: str, *args: object) -> None:
        super().__init__(*args)

        self.benchmark_id = benchmark_id
