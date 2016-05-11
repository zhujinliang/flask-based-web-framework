# -*- coding: utf-8 -*-

import requests
from requests.adapters import HTTPAdapter

from flask import Flask
from flask.ext.cache import Cache
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import  SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from raven.contrib.flask import Sentry
from raven.contrib.flask import Sentry
from redis import Redis

from config import config



def create_app():
    ''' Create flask app.'''

    app = Flask(__name__)

    app.config.from_object(config)

    app.template_folder = app.config['TEMPLATE_FOLDER']
    app.static_folder = app.config['STATIC_FOLDER']

    return app

app = create_app()

# Database config
db = SQLAlchemy(app)

# Redis config
redis = Redis(host=app.config.get('REDIS_SERVER'), \
            port=app.config.get('REDIS_SERVER_PORT'), \
            db=app.config.get('REDIS_DATABASE_INDEX', 0), \
            socket_timeout=app.config.get('REDIS_SOCKET_TIMEOUT', 1), \
            retry_on_timeout=True)

# Cache config
cache_config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': app.config['REDIS_SERVER'],
    'CACHE_REDIS_PORT': app.config['REDIS_SERVER_PORT'],
    'CACHE_REDIS_DB': app.config['REDIS_DATABASE_INDEX'],
    'CACHE_DEFAULT_TIMEOUT': app.config['REDIS_SOCKET_TIMEOUT'],
    'CACHE_KEY_PREFIX': app.config['CACHE_KEY_PREFIX'],
}
cache = Cache(app, config=cache_config)

http_pool = requests.Session()
http_pool_with_retry = requests.Session()
http_pool_with_retry.mount('http://', HTTPAdapter(max_retries=1))
# login config
login_manager = LoginManager()
login_manager.setup_app(app)

# Register csrf protect when submit form.
csrf = CsrfProtect(app)

# Mail config
mail = Mail(app)

# sentry
sentry = Sentry(app)


if app.debug:
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)

    if app.config.get('PROFILE', False):
        from werkzeug.contrib.profiler import ProfilerMiddleware
        app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

# Set server error notification.
if not app.debug:
    import logging
    from logging import Formatter
    from logging.handlers import SMTPHandler
    admins = app.config['ADMINS']
    mail_handler = SMTPHandler('smtp.exmail.qq.com',
                               'kuaima_notice@imdada.cn',
                               admins, 'YourApplication Failed',
                               ('kuaima_notice@imdada.cn', 'Gt54rfvb'))
    mail_handler.setLevel(logging.ERROR)
    format = Formatter('''
    Message type:   %(levelname)s <br/>
    Location:   %(pathname)s:%(lineno)d <br/>
    Module:     %(module)s <br/>
    Function:   %(funcName)s <br/>
    Time:       %(asctime)s <br/>

    Message:
    %(message)s
    ''')
    mail_handler.setFormatter(format)
    app.logger.addHandler(mail_handler)
