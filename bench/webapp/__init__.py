# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

web_app_blueprint = Blueprint('client_app',
                              __name__,
                              url_prefix='',
                              static_folder='./assets',
                              template_folder='./templates')


@web_app_blueprint.route('/')
def index():
    return render_template('index.html')
