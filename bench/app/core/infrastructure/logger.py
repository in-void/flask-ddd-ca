# -*- coding: utf-8 -*-

from flask import current_app


class Logger(object):

    def info(self, message: str) -> None:
        raise NotImplementedError()


class FlaskFileLogger(Logger):

    def info(self, message: str) -> None:
        current_app.logger.info(message)
