# -*- coding: utf-8 -*-

from typing import List

from bench.app.core.command_bus.structures import Command


class SendSmsCommand(Command):

    phone_number: str

    message: str

    def __init__(self, phone_number: str, message: str) -> None:
        super().__init__()

        self.message = message
        self.phone_number = phone_number


class SendEmailCommand(Command):

    subject: str

    recipients: List[str]

    content: str

    def __init__(self, subject: str, recipients: List[str], content: str) -> None:
        super().__init__()

        self.content = content
        self.recipients = recipients
        self.subject = subject
