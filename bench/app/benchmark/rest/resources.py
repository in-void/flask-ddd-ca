# -*- coding: utf-8 -*-

import uuid
from flask_restful.reqparse import RequestParser

from bench.app.core.rest.common import BaseResource
from bench.app.benchmark.rest.presenters import ComparativeBenchmarkPresenter
from bench.app.benchmark.use_cases.commands import CreateComparativeWebPagesBenchmarkCommand
from bench.app.config import benchmark_repository

request_parser = RequestParser()
request_parser.add_argument('subject_url', type=str)
request_parser.add_argument('competitors_urls', type=str)


class WebPageBenchmarkResource(BaseResource):

    def get(self, benchmark_id: str):
        pass


class WebPageBenchmarkListResource(BaseResource):

    def post(self):
        request_data = request_parser.parse_args()

        benchmark_id = str(uuid.uuid4())

        command = CreateComparativeWebPagesBenchmarkCommand.from_dict(benchmark_id, request_data)

        self.execute(command)

        benchmark = benchmark_repository.get_by_id(benchmark_id)

        return self.response_created(ComparativeBenchmarkPresenter.from_object(benchmark))