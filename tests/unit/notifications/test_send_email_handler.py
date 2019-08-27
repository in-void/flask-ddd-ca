# -*- coding: utf-8 -*-

from unittest.mock import patch

from bench.app.notifications.use_cases.commands import SendEmailCommand
from bench.app.notifications.use_cases.handlers import SendEmailHandler


@patch('bench.app.notifications.infrastructure.email_sender.EmailSender')
def test_it_should_send_email(email_sender_mock):
    # given
    send_email_command = SendEmailCommand('some subject', ['darthvader@starwars.com'], 'some message')

    # when
    send_email_handler = SendEmailHandler(email_sender_mock)
    send_email_handler.handle(send_email_command)

    # then
    email_sender_mock.send_email.assert_called_once_with(
        send_email_command.subject, send_email_command.recipients, send_email_command.content)
