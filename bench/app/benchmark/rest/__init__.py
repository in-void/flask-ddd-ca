# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api
from bench.app.benchmark.rest.resources import WebPageBenchmarkResource, WebPageBenchmarkListResource

rest_blueprint = Blueprint('api', __name__)

api = Api(rest_blueprint, prefix='/api')

api.add_resource(WebPageBenchmarkResource, '/benchmark/<benchmark_id>')
api.add_resource(WebPageBenchmarkListResource, '/benchmark')
