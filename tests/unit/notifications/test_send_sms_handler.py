# -*- coding: utf-8 -*-

from unittest.mock import patch

from bench.app.notifications.use_cases.commands import SendSmsCommand
from bench.app.notifications.use_cases.handlers import SendSmsHandler


@patch('bench.app.notifications.infrastructure.sms_sender.SmsSender')
def test_it_should_send_sms(sms_sender_mock):
    # given
    send_sms_command = SendSmsCommand('123123123', 'some message')

    # when
    send_sms_handler = SendSmsHandler(sms_sender_mock)
    send_sms_handler.handle(send_sms_command)

    # then
    sms_sender_mock.send_sms.assert_called_once_with(send_sms_command.phone_number, send_sms_command.message)