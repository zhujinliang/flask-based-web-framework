# -*- coding: utf-8 -*-

from core import login_manager
from core.models.user import User
from core.utils.auth import authenticate as _authenticate


__all__ = [
    'authenticate',
]


login_manager.login_view = 'customer_login'
login_manager.login_message = '请登录后再访问该页面。'


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(user_id)


def authenticate(username, raw_password):
    '''
    If User's username and raw_password is valid and right, return a 
    User object.
    '''
    return _authenticate(User, username=username, raw_password=raw_password)
