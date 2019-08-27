# -*- coding: utf-8 -*-


class NotificationsConfig(object):

    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.notification_email = kwargs.get('notification_email')
        self.notification_sms_phone_number = kwargs.get('notification_sms_phone_number')
