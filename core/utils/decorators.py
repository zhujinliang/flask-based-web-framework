# -*- coding: utf-8 -*-

import threading

from functools import update_wrapper
from functools import wraps

from flask.ext.login import current_user
from flask.ext.login import login_required as flask_login_required




__all__ = [
    'async',
    'login_required',
]


class async(object):
    ''' Decorator that turns a callable function into a thread.'''
    __name__ = 'async'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print kwargs
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        thread = threading.Thread(
            target=self.func,
            args=args,
            kwargs=kwargs
        )
        thread.start()
        return True


def _ajax_login_required(func):
    '''
    Verify the user if request is ajax.
    '''
    def verify_login(*args, **kwargs):
        if login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated():
            context = {
                'status': 'fail',
                'msg': u'账号未登陆'
            }
            return make_json_response(context)
        else:
            return func(*args, **kwargs)
    return verify_login


def login_required(ajax=False):
    '''
    Verify the user when request a page.
    '''
    def _login_required(func):
        if ajax:
            return _ajax_login_required(func)
        else:
            return flask_login_required(func)
    return _login_required
