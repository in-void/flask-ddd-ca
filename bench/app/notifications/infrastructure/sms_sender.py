# -*- coding: utf-8 -*-

from smsapi.client import Client


class SmsSender(object):

    def send_sms(self, phone_number, message):
        raise NotImplementedError()


class SmsapiSmsSender(SmsSender):

    def __init__(self, client: Client) -> None:
        super().__init__()

        self.client = client

    def send_sms(self, phone_number: str, message: str) -> None:
        try:
            self.client.sms.send(to=phone_number, message=message)
        except Exception:
            pass
