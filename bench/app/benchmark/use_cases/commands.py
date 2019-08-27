# -*- coding: utf-8 -*-

from typing import List, Dict

from bench.app.core.command_bus.structures import Command


class CreateComparativeWebPagesBenchmarkCommand(Command):

    benchmark_id: str

    subject_url: str

    competitors_urls: List[str]

    @classmethod
    def from_dict(cls, benchmark_id: str, data: Dict):
        command = cls()

        command.benchmark_id = benchmark_id
        command.subject_url = data.get('subject_url')
        command.competitors_urls = data.get('competitors_urls', '').split(',')

        return command
