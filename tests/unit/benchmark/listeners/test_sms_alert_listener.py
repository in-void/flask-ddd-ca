# -*- coding: utf-8 -*-

from unittest.mock import patch

from tests.fixtures.benchmark import ComparativeBenchmarkMother
from bench.app.benchmark.domain.config import NotificationsConfig
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository
from bench.app.benchmark.use_cases.listeners.sms_alert_listener import ComparativeBenchmarkFinishedSmsAlertListener
from bench.app.notifications.use_cases.commands import SendSmsCommand

notifications_config = NotificationsConfig(notification_sms_phone_number='some number')


@patch('bench.app.benchmark.domain.specification.SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification')
def test_it_should_send_sms_if_subject_url_loaded_twice_as_slow_as_at_least_one_of_competitors(specification_mock):
    # given
    specification_mock.is_satisfied_by.return_value = True
    benchmark = ComparativeBenchmarkMother.create_any()

    # and
    repository = ComparativeBenchmarkInMemoryRepository()
    repository.add(benchmark)

    # when
    listener = ComparativeBenchmarkFinishedSmsAlertListener(notifications_config, specification_mock, repository)
    result = listener.execute(ComparativeBenchmarkFinished(benchmark.benchmark_id))

    # then
    expected_command = SendSmsCommand(notifications_config.notification_sms_phone_number, 'Your site is very slow')
    assert expected_command == result


@patch('bench.app.benchmark.domain.specification.SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification')
def test_it_should_not_send_sms_if_subject_url_loaded_faster_than_competitors(specification_mock):
    # given
    specification_mock.is_satisfied_by.return_value = False
    benchmark = ComparativeBenchmarkMother.create_any()

    # and
    repository = ComparativeBenchmarkInMemoryRepository()
    repository.add(benchmark)

    # when
    listener = ComparativeBenchmarkFinishedSmsAlertListener(notifications_config, specification_mock, repository)
    result = listener.execute(ComparativeBenchmarkFinished(benchmark.benchmark_id))

    # then
    assert result is None
