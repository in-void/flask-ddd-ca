# -*- coding: utf-8 -*-

from typing import List

from bench.app.core.command_bus.structures import Command


class DomainEvent(object):

    def __eq__(self, o: object) -> bool:
        if isinstance(self, o.__class__):
            return self.__dict__ == o.__dict__
        return False


class DomainEventsDispatcherMixin(object):

    def __init__(self) -> None:
        super().__init__()

        self.events = []

    def fire_event(self, domain_event: DomainEvent) -> None:
        self.events.append(domain_event)

    def release_events(self) -> List:
        events = self.events

        self.events = []

        return events


class DomainEventsListener(object):

    def execute(self, event: DomainEvent):
        raise NotImplementedError()


class EventDispatcher(object):

    def __init__(self) -> None:
        super().__init__()

        self._listeners = {}
        self.command_bus = None

    def dispatch(self, event: DomainEvent = None):
        print(self._listeners[event.name])

        for listener in self._listeners[event.name]:
            result = listener.execute(event)

            if isinstance(result, Command) and self.command_bus:
                self.command_bus.execute(result)

    def dispatch_events(self, events: List):
        for event in events:
            self.dispatch(event)

    def add_listener(self, event_name: str, listener: DomainEventsListener) -> None:
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)
