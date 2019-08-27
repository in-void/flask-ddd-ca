# -*- coding: utf-8 -*-

from unittest.mock import patch

from tests.fixtures.benchmark import ComparativeBenchmarkMother
from bench.app.benchmark.domain.config import NotificationsConfig
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository
from bench.app.benchmark.use_cases.listeners.email_alert_listener import ComparativeBenchmarkFinishedEmailAlertListener
from bench.app.notifications.use_cases.commands import SendEmailCommand

notifications_config = NotificationsConfig(notification_email='some email')


@patch('bench.app.benchmark.domain.specification.SubjectLoadedSlowerThanAtLeastOneOfCompetitorsSpecification')
def test_it_should_send_email_if_subject_url_loaded_slower_than_at_least_one_of_competitors(specification_mock):
    # given
    specification_mock.is_satisfied_by.return_value = True
    benchmark = ComparativeBenchmarkMother.create_any()

    # and
    repository = ComparativeBenchmarkInMemoryRepository()
    repository.add(benchmark)

    # when
    listener = ComparativeBenchmarkFinishedEmailAlertListener(notifications_config, specification_mock, repository)
    result = listener.execute(ComparativeBenchmarkFinished(benchmark.benchmark_id))

    # then
    expected_command = SendEmailCommand('Benchmark alert', [notifications_config.notification_email], 'Your site is slow')
    assert expected_command == result


@patch('bench.app.benchmark.domain.specification.SubjectLoadedSlowerThanAtLeastOneOfCompetitorsSpecification')
def test_it_should_not_send_email_if_subject_url_loaded_faster_than_competitors(specification_mock):
    # given
    specification_mock.is_satisfied_by.return_value = False
    benchmark = ComparativeBenchmarkMother.create_any()

    # and
    repository = ComparativeBenchmarkInMemoryRepository()
    repository.add(benchmark)

    # when
    listener = ComparativeBenchmarkFinishedEmailAlertListener(notifications_config, specification_mock, repository)
    result = listener.execute(ComparativeBenchmarkFinished(benchmark.benchmark_id))

    # then
    assert result is None
