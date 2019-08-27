# -*- coding: utf-8 -*-

import os
import logging
from flask import Flask
from logging.handlers import RotatingFileHandler

from bench.configuration import Configuration
from bench.app.benchmark.rest import rest_blueprint
from bench.extensions import mail
from bench.webapp import web_app_blueprint


def create_app(configuration_object: Configuration = Configuration) -> Flask:

    app = Flask(__name__)

    app.config.from_object(configuration_object)

    register_logger_handlers(app)

    mail.init_app(app)

    app.register_blueprint(rest_blueprint)
    app.register_blueprint(web_app_blueprint)

    return app


def register_logger_handlers(app):

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(curr_dir, '../', 'logs', 'log.txt')

    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024 * 100, backupCount=1)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("\n%(message)s")
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)
