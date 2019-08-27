# -*- coding: utf-8 -*-

import time
import urllib.request

from bench.app.benchmark.domain.value_objects import PageBenchmark


class PageBenchmarker(object):

    def measure_page_load(self, url: str) -> PageBenchmark:
        raise NotImplementedError()


class UrllibPageBenchmarker(PageBenchmarker):

    def measure_page_load(self, url: str) -> PageBenchmark:
        uri = self.normalize_url(url)

        opened_url = urllib.request.urlopen(uri)

        start_time = time.time()
        opened_url.read()
        end_time = time.time()

        opened_url.close()

        load_time: float = end_time - start_time

        return PageBenchmark(uri, load_time)

    def normalize_url(self, url: str) -> str:
        if url.startswith('http://'):
            return url

        if url.startswith('https://'):
            return url

        return 'http://' + url
