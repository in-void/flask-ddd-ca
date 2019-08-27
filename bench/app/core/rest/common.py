# -*- coding: utf-8 -*-

from typing import Tuple, Dict

from flask_restful import Resource

from bench.app.config import command_bus


class BaseResource(Resource):

    def execute(self, command: object) -> None:
        command_bus.execute(command)

    def find(self, query: object) -> None:
        pass

    def response_created(self, presenter: Dict) -> Tuple[dict, int]:
        return presenter, 201

    def response_ok(self, presenter: Dict) -> Tuple[dict, int]:
        return presenter, 200
