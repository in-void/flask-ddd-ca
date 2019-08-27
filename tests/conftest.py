# -*- coding: utf-8 -*-

import pytest

from bench.app_factory import create_app


@pytest.yield_fixture(scope='function')
def app():
    app = create_app()

    ctx = app.app_context()
    ctx.push()

    return app
