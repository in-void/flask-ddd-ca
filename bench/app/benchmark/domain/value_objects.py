# -*- coding: utf-8 -*-

from bench.app.core.domain import ValueObject


class PageBenchmark(ValueObject):

    def __init__(self, url: str, load_time: float) -> None:
        super().__init__()

        self.url = url
        self.load_time = load_time
