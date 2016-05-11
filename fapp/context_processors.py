# -*- coding: utf-8 -*-

from core import app


@app.context_processor
def inject_config():
    context = {
        'STATIC_URL': app.config['STATIC_URL_ROOT']
    }
    return context
