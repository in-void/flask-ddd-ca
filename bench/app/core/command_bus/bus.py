# -*- coding: utf-8 -*-

from typing import Type

from bench.app.core.command_bus.structures import Command


class CommandMapping(dict):

    def register_command(self, command: Type, handler: object) -> None:
        self[command] = handler


class CommandBus(object):

    def __init__(self, middlewares) -> None:
        super().__init__()

        self.middlewares = middlewares

    def execute(self, command: Command):
        self.middlewares.execute(command)
