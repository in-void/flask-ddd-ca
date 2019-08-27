# -*- coding: utf-8 -*-

from typing import List
from flask_mail import Message

from bench.extensions import mail


class EmailSender(object):

    def send_email(self, subject: str, recipients: List[str], content: str):
        raise NotImplementedError()


class FlaskEmailSender(EmailSender):

    def send_email(self, subject: str, recipients: List[str], content: str) -> None:
        try:
            message = Message(subject=subject, recipients=recipients, body=content)
            mail.send(message)
        except Exception:
            pass
