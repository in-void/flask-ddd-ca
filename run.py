# -*- coding: utf-8 -*-

from bench.app_factory import create_app

app = create_app()

app.run(port=5000, debug=True)
