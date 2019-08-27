# -*- coding: utf-8 -*-

from bench.app.notifications.infrastructure.email_sender import EmailSender
from bench.app.notifications.infrastructure.sms_sender import SmsSender
from bench.app.notifications.use_cases.commands import SendSmsCommand, SendEmailCommand


class SendSmsHandler(object):

    def __init__(self, sms_sender: SmsSender) -> None:
        super().__init__()

        self.sms_sender = sms_sender

    def handle(self, command: SendSmsCommand):
        self.sms_sender.send_sms(command.phone_number, command.message)


class SendEmailHandler(object):

    def __init__(self, email_sender: EmailSender) -> None:
        self.email_sender = email_sender

    def handle(self, command: SendEmailCommand):
        self.email_sender.send_email(command.subject, command.recipients, command.content)
