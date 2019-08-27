# -*- coding: utf-8 -*-

from unittest.mock import patch

from bench.app.notifications.infrastructure.email_sender import FlaskEmailSender


@patch('bench.extensions.mail.send')
def test_it_should_send_email(mail_send_mock):
    # given
    some_subject, some_recipients, some_content = 'subject', ['recipient'], 'content'

    # when
    email_sender = FlaskEmailSender()
    email_sender.send_email(some_subject, some_recipients, some_content)

    # then
    mail_send_mock.assert_called()