# -*- coding: utf-8 -*-

from smsapi.client import SmsApiPlClient

from bench.app.benchmark.domain.config import NotificationsConfig
from bench.app.benchmark.domain.events import ComparativeBenchmarkFinished
from bench.app.benchmark.domain.specification import SubjectLoadedSlowerThanAtLeastOneOfCompetitorsSpecification, \
    SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification
from bench.app.benchmark.infrastructure.page_benchmark import UrllibPageBenchmarker
from bench.app.benchmark.infrastructure.repositories import ComparativeBenchmarkInMemoryRepository
from bench.app.benchmark.use_cases.listeners.email_alert_listener import ComparativeBenchmarkFinishedEmailAlertListener
from bench.app.benchmark.use_cases.listeners.logger_listener import ComparativeBenchmarkFinishedLoggerListener
from bench.app.benchmark.use_cases.listeners.sms_alert_listener import ComparativeBenchmarkFinishedSmsAlertListener
from bench.app.core.command_bus.bus import CommandBus, CommandMapping
from bench.app.core.command_bus.middlewares import DomainEventsDispatcherDecorator, CommandExecutorMiddleware, \
    CommandLoggingMiddleware
from bench.app.benchmark.use_cases.commands import CreateComparativeWebPagesBenchmarkCommand
from bench.app.benchmark.use_cases.handlers import CreateComparativeWebPagesBenchmarkHandler
from bench.app.core.domain.events_dispatcher import EventDispatcher
from bench.app.core.infrastructure.logger import FlaskFileLogger
from bench.app.notifications.infrastructure.email_sender import FlaskEmailSender
from bench.app.notifications.infrastructure.sms_sender import SmsapiSmsSender

from bench.app.notifications.use_cases.commands import SendSmsCommand, SendEmailCommand
from bench.app.notifications.use_cases.handlers import SendSmsHandler, SendEmailHandler
from bench.configuration import Configuration

command_mapping = CommandMapping()

logger = FlaskFileLogger()

smsapi_client = SmsApiPlClient(access_token=Configuration.SMSAPI_ACCESS_TOKEN)

sms_sender = SmsapiSmsSender(smsapi_client)
email_sender = FlaskEmailSender()

page_benchmarker = UrllibPageBenchmarker()
benchmark_repository = ComparativeBenchmarkInMemoryRepository()
benchmark_handler = CreateComparativeWebPagesBenchmarkHandler(benchmark_repository, page_benchmarker)

command_mapping.register_command(CreateComparativeWebPagesBenchmarkCommand, benchmark_handler)
command_mapping.register_command(SendSmsCommand, SendSmsHandler(sms_sender))
command_mapping.register_command(SendEmailCommand, SendEmailHandler(email_sender))

benchmark_twice_slower_specification = SubjectLoadedTwiceAsSlowThanAtLeastOfCompetitorsSpecification()
benchmark_slow_load_specification = SubjectLoadedSlowerThanAtLeastOneOfCompetitorsSpecification()

notifications_config = NotificationsConfig(
    notification_email=Configuration.NOTIFICATION_EMAIL,
    notification_sms_phone_number=Configuration.NOTIFICATION_SMS_PHONE_NUMBER,
)

benchmark_logger_listener = ComparativeBenchmarkFinishedLoggerListener(benchmark_repository, logger)

benchmark_sms_alert_listener = ComparativeBenchmarkFinishedSmsAlertListener(
    notifications_config, benchmark_twice_slower_specification, benchmark_repository)

benchmark_email_alert_listener = ComparativeBenchmarkFinishedEmailAlertListener(
    notifications_config, benchmark_slow_load_specification, benchmark_repository)

domain_event_dispatcher = EventDispatcher()

domain_event_dispatcher.add_listener(ComparativeBenchmarkFinished.name, benchmark_sms_alert_listener)
domain_event_dispatcher.add_listener(ComparativeBenchmarkFinished.name, benchmark_email_alert_listener)
domain_event_dispatcher.add_listener(ComparativeBenchmarkFinished.name, benchmark_logger_listener)

command_loggin_middleware = CommandLoggingMiddleware(logger)
command_bus_middlewares = CommandExecutorMiddleware(command_mapping, command_loggin_middleware)

command_executor_middleware = DomainEventsDispatcherDecorator(domain_event_dispatcher,
                                                              command_mapping,
                                                              command_bus_middlewares)

command_bus = CommandBus(command_executor_middleware)

domain_event_dispatcher.command_bus = command_bus