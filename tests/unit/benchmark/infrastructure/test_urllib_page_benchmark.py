# -*- coding: utf-8 -*-

from unittest.mock import Mock, patch

from bench.app.benchmark.infrastructure.page_benchmark import UrllibPageBenchmarker

page_benchmark = UrllibPageBenchmarker()


@patch('urllib.request.urlopen')
def test_it_should_measure_page_load_time(urlopen_mock):
    # given
    urlopen_context_mock = Mock()
    urlopen_mock.return_value = urlopen_context_mock

    some_url = 'https://www.google.com'

    # when
    benchmark = page_benchmark.measure_page_load(some_url)

    # then
    urlopen_mock.assert_called_once_with(some_url)
    urlopen_context_mock.read.assert_called_once()

    assert benchmark.url == some_url
    assert isinstance(benchmark.load_time, float)


@patch('urllib.request.urlopen')
def test_it_should_normalize_url(urlopen_mock):
    # given
    urlopen_context_mock = Mock()
    urlopen_mock.return_value = urlopen_context_mock

    some_url = 'www.google.com'

    # when
    benchmark = page_benchmark.measure_page_load(some_url)

    # then
    assert benchmark.url == 'http://' + some_url
