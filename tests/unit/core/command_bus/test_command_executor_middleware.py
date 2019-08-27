# -*- coding: utf-8 -*-

from unittest.mock import Mock

from bench.app.core.command_bus.bus import CommandMapping
from bench.app.core.command_bus.structures import Command
from bench.app.core.command_bus.middlewares import CommandExecutorMiddleware


def test_it_should_inform_when_handler_not_found_for_command():
    # given
    not_mapped_command = Command()
    commands_mapping = CommandMapping()

    # then
    try:
        command_executor = CommandExecutorMiddleware(commands_mapping)
        command_executor.execute(not_mapped_command)
        assert False
    except RuntimeError:
        assert True


def test_it_should_find_handler_for_command():
    # given
    command_handler = Mock()
    commands_mapping = CommandMapping()
    commands_mapping.register_command(Command, command_handler)

    #  when
    command_executor = CommandExecutorMiddleware(commands_mapping)
    command_executor.execute(Command())

    # then
    command_handler.handle.assert_called_once_with(Command())