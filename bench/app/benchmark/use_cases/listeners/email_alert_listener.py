# -*- coding: utf-8 -*-

from bench.app.benchmark.domain.config import NotificationsConfig
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkRepository
from bench.app.core.domain.events_dispatcher import DomainEventsListener
from bench.app.core.domain.specification import Specification
from bench.app.notifications.use_cases.commands import SendEmailCommand


class ComparativeBenchmarkFinishedEmailAlertListener(DomainEventsListener):

    def __init__(self,
                 config: NotificationsConfig,
                 specification: Specification,
                 benchmark_repository: ComparativeBenchmarkRepository) -> None:

        super().__init__()

        self.config = config
        self.specification = specification
        self.benchmark_repository = benchmark_repository

    def execute(self, event: ComparativeBenchmarkFinished):
        benchmark = self.benchmark_repository.get_by_id(event.benchmark_id)

        if self.specification.is_satisfied_by(benchmark):
            return self.send_email()

    def send_email(self):
        return SendEmailCommand('Benchmark alert', [self.config.notification_email], 'Your site is slow')
