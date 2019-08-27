# -*- coding: utf-8 -*-

from typing import Dict

from bench.app.core.command_bus.structures import Command
from bench.app.core.domain.events_dispatcher import EventDispatcher, DomainEventsDispatcherMixin
from bench.app.core.infrastructure.logger import Logger


class Middleware(object):

    def __init__(self, next_middleware = None) -> None:
        super().__init__()

        self.next_middleware = next_middleware

    def execute(self, command: Command):
        raise NotImplementedError()

    def next(self, command):
        if self.next_middleware:
            self.next_middleware.execute(command)


class CommandExecutorMiddleware(Middleware):

    def __init__(self, commands_mapping: Dict, next_middleware = None) -> None:
        super().__init__(next_middleware)

        self.commands_mapping = commands_mapping

    def execute(self, command: Command):
        handler = self.commands_mapping.get(type(command))

        if not handler:
            raise RuntimeError('Handler for command<%s> not found' % command)

        handler.handle(command)

        self.next(command)


class CommandLoggingMiddleware(Middleware):

    def __init__(self, logger: Logger, next_middleware=None) -> None:
        super().__init__(next_middleware)

        self.logger = logger

    def execute(self, command: Command) -> None:
        message = '%s: %s' % (command.__class__.__name__, str(command.__dict__))

        self.logger.info(message)


class DomainEventsDispatcherDecorator(Middleware):

    def __init__(self, events_dispatcher: EventDispatcher, commands_mapping: Dict, middleware: Middleware) -> None:

        super().__init__(middleware)

        self.events_dispatcher = events_dispatcher
        self.middleware = middleware
        self.commands_mapping = commands_mapping

    def execute(self, command: Command):
        handler = self.commands_mapping.get(type(command))

        self.middleware.execute(command)

        if isinstance(handler, DomainEventsDispatcherMixin):
            events = handler.release_events()
            self.events_dispatcher.dispatch_events(events)
