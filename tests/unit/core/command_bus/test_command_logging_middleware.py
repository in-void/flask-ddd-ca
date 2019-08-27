# -*- coding: utf-8 -*-

from unittest.mock import patch

from bench.app.core.command_bus.structures import Command
from bench.app.core.command_bus.middlewares import CommandLoggingMiddleware


class SomeCommand(Command):
    attr1: str

    attr2: str


@patch('bench.app.core.infrastructure.logger')
def test_it_hsould_log_command_attributes(logger_mock):
    # given
    some_command = SomeCommand()
    some_command.attr1 = 'a1'
    some_command.attr2 = 2

    # when
    logging_middleware = CommandLoggingMiddleware(logger_mock)
    logging_middleware.execute(some_command)

    # then
    logger_mock.info.assert_called_once_with("SomeCommand: {'attr1': 'a1', 'attr2': 2}")
