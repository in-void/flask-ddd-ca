# -*- coding: utf-8 -*-

from bench.app.core.domain.events_dispatcher import DomainEventsDispatcherMixin, DomainEvent

some_event = DomainEvent()
domain_events_dispatcher_mixin = DomainEventsDispatcherMixin()


def test_it_should_store_events():
    # when
    domain_events_dispatcher_mixin.fire_event(some_event)

    # then
    assert domain_events_dispatcher_mixin.release_events() == [some_event]


def test_it_should_clear_events_after_release():
    # when
    domain_events_dispatcher_mixin.fire_event(some_event)
    domain_events_dispatcher_mixin.release_events()

    # then
    assert domain_events_dispatcher_mixin.events == []