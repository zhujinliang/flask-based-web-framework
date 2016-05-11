# -*- encoding:utf8 -*-

import os


PROJECT_PATH = os.path.abspath(
                    os.path.join(
                        os.path.abspath(os.path.dirname(__file__)),
                        os.pardir, os.pardir))



class Config(object):

    TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, 'fapp/templates')
    STATIC_FOLDER = os.path.join(PROJECT_PATH, 'fapp/static')

    STATIC_URL_ROOT = '/static/'

    SECRET_KEY = 'your_secret_key'


    DFINANCE_PRIVATE_KEY = '12345'

    AUTH_HASH_SALT = 'your_auth_hash_salt'  # for set and check password hash

    ADMINS = ['test@yourdomain.com', ]

    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_DATABASE_URI = 'mysql://test:test@127.0.0.1/test'

    # Redis config.
    REDIS_SERVER = '127.0.0.1'
    REDIS_SERVER_PORT = '6379'
    REDIS_DATABASE_INDEX = 0
    REDIS_SOCKET_TIMEOUT = 1

    REDIS_EXPIRE_TIME_SHORT = 180  # 3min = 60 * 3
    REDIS_EXPIRE_TIME_MIDDLE = 3600  # 1hour = 60 * 60
    REDIS_EXPIRE_TIME_LONG = 86400  # 1d = 60 * 60 * 24

    # Cache config.
    CACHE_DEFAULT_TIMEOUT = 3600
    CACHE_KEY_PREFIX = 'test'

    # Session config.
    SESSION_COOKIE_NAME = 'sessionid'
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = 864000  # 10day = 3600 * 24 * 10

    SENTRY_DSN = 'http://test:test@sentry.yourdomain.com/1'

    # WTForm config.
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'your_csrf_secret_key'

    # Mail config.
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_USERNAME = 'test@yourdomain.com'
    MAIL_PASSWORD = 'your_email_password'
    MAIL_SENDER = 'test@yourdomain.com'

